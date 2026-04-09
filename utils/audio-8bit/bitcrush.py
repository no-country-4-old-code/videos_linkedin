"""
bitcrush.py — 8-bit audio converter

Converts mp3, mp4, or wav audio files into a retro 8-bit / chiptune sound.
Requires ffmpeg to be installed on the system.

Usage:
    python bitcrush.py input.mp3 [options]
    python bitcrush.py --help
"""

import argparse
import sys
from math import gcd
from pathlib import Path

import numpy as np
from pydub import AudioSegment
from scipy.signal import butter, sosfilt, resample, resample_poly

SUPPORTED_INPUTS = {".mp3", ".mp4", ".wav"}
SUPPORTED_OUTPUTS = {".mp3", ".wav"}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="bitcrush",
        description="Convert audio to an 8-bit / chiptune sound.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("input", help="Input audio file (.mp3, .mp4, .wav)")
    p.add_argument(
        "-o", "--output",
        default=None,
        help="Output file path. Defaults to {input_stem}_8bit.wav",
    )
    p.add_argument(
        "-sr", "--sample-rate",
        type=int,
        default=11025,
        metavar="HZ",
        help="Target sample rate in Hz (2000–44100). Lower = more lo-fi.",
    )
    p.add_argument(
        "-bd", "--bit-depth",
        type=int,
        default=8,
        metavar="BITS",
        help="Bit depth for quantization (2–16). Lower = crunchier.",
    )
    p.add_argument(
        "-ps", "--pitch-shift",
        type=float,
        default=1.0,
        metavar="FACTOR",
        help="Pitch shift factor (0.25–4.0). >1.0 = higher pitch.",
    )
    p.add_argument(
        "-lp", "--lowpass-cutoff",
        type=int,
        default=None,
        metavar="HZ",
        help="Low-pass filter cutoff in Hz. Defaults to sample_rate * 0.45.",
    )
    p.add_argument(
        "-ws", "--wave-shaping",
        type=float,
        default=0.0,
        metavar="INTENSITY",
        help="Wave shaping intensity (0.0–1.0). Pushes toward square wave.",
    )
    p.add_argument(
        "-n", "--normalize",
        action="store_true",
        help="Normalize output volume.",
    )
    return p


def validate_args(args: argparse.Namespace) -> bool:
    ok = True

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file not found: {args.input}", file=sys.stderr)
        ok = False
    elif input_path.suffix.lower() not in SUPPORTED_INPUTS:
        print(
            f"Error: unsupported input format '{input_path.suffix}'. "
            f"Supported: {', '.join(sorted(SUPPORTED_INPUTS))}",
            file=sys.stderr,
        )
        ok = False

    if args.output is None:
        args.output = str(input_path.with_name(input_path.stem + "_8bit.wav"))
    else:
        out_ext = Path(args.output).suffix.lower()
        if out_ext not in SUPPORTED_OUTPUTS:
            print(
                f"Error: unsupported output format '{out_ext}'. "
                f"Supported: {', '.join(sorted(SUPPORTED_OUTPUTS))}",
                file=sys.stderr,
            )
            ok = False

    if not (2000 <= args.sample_rate <= 44100):
        print(
            f"Warning: sample rate {args.sample_rate} Hz is outside the "
            "recommended range (2000–44100). Clamping.",
            file=sys.stderr,
        )
        args.sample_rate = max(2000, min(44100, args.sample_rate))

    if not (2 <= args.bit_depth <= 16):
        print(
            f"Warning: bit depth {args.bit_depth} is outside the range "
            "2–16. Clamping.",
            file=sys.stderr,
        )
        args.bit_depth = max(2, min(16, args.bit_depth))

    if not (0.25 <= args.pitch_shift <= 4.0):
        print(
            f"Warning: pitch shift {args.pitch_shift} is outside the range "
            "0.25–4.0. Clamping.",
            file=sys.stderr,
        )
        args.pitch_shift = max(0.25, min(4.0, args.pitch_shift))

    if not (0.0 <= args.wave_shaping <= 1.0):
        print(
            f"Warning: wave shaping {args.wave_shaping} is outside 0.0–1.0. "
            "Clamping.",
            file=sys.stderr,
        )
        args.wave_shaping = max(0.0, min(1.0, args.wave_shaping))

    if args.lowpass_cutoff is not None:
        nyquist = args.sample_rate / 2
        if args.lowpass_cutoff >= nyquist:
            clamped = int(nyquist * 0.9)
            print(
                f"Warning: lowpass cutoff {args.lowpass_cutoff} Hz >= "
                f"Nyquist ({nyquist:.0f} Hz). Clamping to {clamped} Hz.",
                file=sys.stderr,
            )
            args.lowpass_cutoff = clamped

    return ok


# ---------------------------------------------------------------------------
# Audio I/O
# ---------------------------------------------------------------------------

def load_audio(filepath: str) -> tuple[np.ndarray, int]:
    """Load audio file to a float64 numpy array in [-1, 1] and its sample rate."""
    print(f'Loading "{filepath}"...')
    try:
        audio = AudioSegment.from_file(filepath)
    except FileNotFoundError:
        print(
            "Error: ffmpeg not found. Install it with:\n"
            "  Ubuntu/Debian: sudo apt install ffmpeg\n"
            "  Windows:       choco install ffmpeg  (or download from ffmpeg.org)\n"
            "  macOS:         brew install ffmpeg",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as exc:
        print(f"Error loading audio: {exc}", file=sys.stderr)
        sys.exit(1)

    original_channels = audio.channels
    original_sr = audio.frame_rate
    duration_s = len(audio) / 1000.0
    mins, secs = divmod(int(duration_s), 60)
    print(
        f"  Duration: {mins}:{secs:02d}, "
        f"Sample Rate: {original_sr} Hz, "
        f"Channels: {original_channels} -> mono"
    )

    # Force mono, 16-bit for clean float conversion
    audio = audio.set_channels(1).set_sample_width(2)
    samples = np.array(audio.get_array_of_samples(), dtype=np.float64)
    samples /= 32768.0  # Normalize int16 to [-1, 1]
    return samples, original_sr


def export_audio(samples: np.ndarray, sample_rate: int, output_path: str) -> None:
    """Export a float64 numpy array in [-1, 1] to an audio file."""
    print(f'Exporting to "{output_path}"...')
    pcm = np.int16(np.clip(samples, -1.0, 1.0) * 32767)
    audio = AudioSegment(
        data=pcm.tobytes(),
        sample_width=2,
        frame_rate=sample_rate,
        channels=1,
    )
    fmt = Path(output_path).suffix.lstrip(".").lower()
    if fmt == "mp4":
        fmt = "wav"
    audio.export(output_path, format=fmt)
    size_kb = Path(output_path).stat().st_size / 1024
    print(f"Done! Output: {output_path} ({size_kb:.1f} KB)")


# ---------------------------------------------------------------------------
# DSP pipeline stages
# ---------------------------------------------------------------------------

def apply_pitch_shift(samples: np.ndarray, factor: float) -> np.ndarray:
    """Shift pitch by resampling the signal to a different length."""
    if factor == 1.0:
        return samples
    new_length = max(1, int(len(samples) / factor))
    return resample(samples, new_length)


def apply_lowpass_filter(
    samples: np.ndarray, cutoff_hz: float, sample_rate: int
) -> np.ndarray:
    """Apply a 5th-order Butterworth low-pass filter."""
    nyquist = sample_rate / 2.0
    normalized_cutoff = cutoff_hz / nyquist
    normalized_cutoff = min(normalized_cutoff, 0.99)
    sos = butter(5, normalized_cutoff, btype="low", output="sos")
    return sosfilt(sos, samples)


def apply_downsample(
    samples: np.ndarray, original_sr: int, target_sr: int
) -> np.ndarray:
    """Downsample using polyphase resampling."""
    if original_sr == target_sr:
        return samples
    g = gcd(original_sr, target_sr)
    up = target_sr // g
    down = original_sr // g
    # Cap factors to keep computation reasonable
    max_factor = 512
    if up > max_factor or down > max_factor:
        scale = max(up, down) / max_factor
        up = max(1, int(up / scale))
        down = max(1, int(down / scale))
    return resample_poly(samples, up, down)


def apply_bitcrush(samples: np.ndarray, bit_depth: int) -> np.ndarray:
    """Quantize signal to the given bit depth, creating the stepped 8-bit sound."""
    levels = 2 ** bit_depth
    half = levels / 2.0
    crushed = np.round(samples * half) / half
    return np.clip(crushed, -1.0, 1.0)


def apply_wave_shaping(samples: np.ndarray, intensity: float) -> np.ndarray:
    """Blend tanh soft-clip with hard square-wave clipping."""
    if intensity == 0.0:
        return samples
    gain = 1.0 + intensity * 20.0
    soft = np.tanh(samples * gain)
    hard = np.sign(samples)
    shaped = soft * (1.0 - intensity) + hard * intensity
    return np.clip(shaped, -1.0, 1.0)


def apply_normalize(samples: np.ndarray, target_peak: float = 0.95) -> np.ndarray:
    peak = np.max(np.abs(samples))
    if peak > 0:
        samples = samples * (target_peak / peak)
    return samples


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def process_audio(
    samples: np.ndarray,
    original_sr: int,
    target_sr: int,
    bit_depth: int,
    pitch_shift: float,
    lowpass_cutoff: int | None,
    wave_shaping: float,
    normalize: bool,
) -> tuple[np.ndarray, int]:
    current_sr = original_sr

    # Stage 1: Pitch shift (on full-resolution data)
    if pitch_shift != 1.0:
        print(f"Applying pitch shift (factor: {pitch_shift})...")
        samples = apply_pitch_shift(samples, pitch_shift)

    # Stage 2: Low-pass filter (anti-aliasing + retro bandwidth limiting)
    if lowpass_cutoff is None:
        lowpass_cutoff = int(target_sr * 0.45)
    # Ensure cutoff is below the Nyquist of the current (pre-downsample) rate
    effective_cutoff = min(lowpass_cutoff, int(current_sr * 0.49))
    print(f"Applying low-pass filter (cutoff: {effective_cutoff} Hz)...")
    samples = apply_lowpass_filter(samples, effective_cutoff, current_sr)

    # Stage 3: Downsample
    print(f"Downsampling: {current_sr} Hz -> {target_sr} Hz...")
    samples = apply_downsample(samples, current_sr, target_sr)
    current_sr = target_sr

    # Stage 4: Bit crush
    print(f"Applying bit crush ({bit_depth}-bit, {2**bit_depth} levels)...")
    samples = apply_bitcrush(samples, bit_depth)

    # Stage 5: Wave shaping
    if wave_shaping > 0.0:
        print(f"Applying wave shaping (intensity: {wave_shaping})...")
        samples = apply_wave_shaping(samples, wave_shaping)

    # Stage 6: Normalize
    if normalize:
        print("Normalizing output...")
        samples = apply_normalize(samples)

    return samples, current_sr


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not validate_args(args):
        return 1

    print()
    print("Settings:")
    print(f"  Sample rate : {args.sample_rate} Hz")
    print(f"  Bit depth   : {args.bit_depth}-bit")
    print(f"  Pitch shift : {args.pitch_shift}x")
    lp_display = args.lowpass_cutoff if args.lowpass_cutoff else f"auto ({int(args.sample_rate * 0.45)} Hz)"
    print(f"  Low-pass    : {lp_display}")
    print(f"  Wave shape  : {args.wave_shaping}")
    print(f"  Normalize   : {args.normalize}")
    print()

    samples, original_sr = load_audio(args.input)

    samples, out_sr = process_audio(
        samples=samples,
        original_sr=original_sr,
        target_sr=args.sample_rate,
        bit_depth=args.bit_depth,
        pitch_shift=args.pitch_shift,
        lowpass_cutoff=args.lowpass_cutoff,
        wave_shaping=args.wave_shaping,
        normalize=args.normalize,
    )

    export_audio(samples, out_sr, args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
