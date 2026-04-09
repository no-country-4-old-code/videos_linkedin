# bitcrush.py — 8-Bit Audio Converter

Convert any mp3, mp4, or wav file into a retro 8-bit / chiptune sound.

## Requirements

**Python packages:**
```bash
pip install -r requirements.txt
```

**System dependency — ffmpeg** (required by pydub for audio decoding):

| Platform | Command |
|---|---|
| Ubuntu/Debian | `sudo apt install ffmpeg` |
| Windows | `choco install ffmpeg` or download from [ffmpeg.org](https://ffmpeg.org/download.html) |
| macOS | `brew install ffmpeg` |

## Usage

```
python bitcrush.py <input> [options]
```

### Options

| Flag | Default | Description |
|---|---|---|
| `-o, --output` | `{stem}_8bit.wav` | Output file path |
| `-sr, --sample-rate` | `11025` | Target sample rate in Hz (2000–44100). Lower = more lo-fi. |
| `-bd, --bit-depth` | `8` | Quantization bit depth (2–16). Lower = crunchier. |
| `-ps, --pitch-shift` | `1.0` | Pitch factor (0.25–4.0). `>1.0` = higher pitch. |
| `-lp, --lowpass-cutoff` | auto | Low-pass filter cutoff in Hz. |
| `-ws, --wave-shaping` | `0.0` | Square-wave intensity (0.0–1.0). |
| `-n, --normalize` | off | Normalize output volume. |

## Examples

### Basic conversion (default 8-bit settings)
```bash
python bitcrush.py song.mp3
```

### Subtle retro effect
```bash
python bitcrush.py song.mp3 -sr 22050 -bd 12
```

### Aggressive chiptune
```bash
python bitcrush.py song.mp3 -sr 8000 -bd 4 -ps 1.5 -ws 0.7 -n
```

---

## How to Generate Retro Game Boy Sound

The original Nintendo Game Boy (DMG-01, 1989) used a custom sound chip with:

- **Sample rate**: ~11468 Hz (wave channel) / 22050 Hz mixed output
- **Bit depth**: 4-bit samples for wave channel, 1-bit for noise
- **Frequency range**: Limited to ~20 Hz – 5500 Hz
- **Character**: Square/pulse waves with strong harmonic distortion

### Recommended settings

```bash
python bitcrush.py song.mp3 \
  -o song_gameboy.wav \
  -sr 11025 \
  -bd 4 \
  -lp 5500 \
  -ws 0.65 \
  -n
```

| Parameter | Value | Reason |
|---|---|---|
| `--sample-rate 11025` | ~11 kHz | Matches the Game Boy wave channel sample rate |
| `--bit-depth 4` | 4-bit | Game Boy wave RAM is 4-bit per sample |
| `--lowpass-cutoff 5500` | 5500 Hz | Emulates the limited bandwidth of the Game Boy speaker and DAC |
| `--wave-shaping 0.65` | 65% | Pushes the waveform toward the square/pulse shape the Game Boy produces |
| `--normalize` | on | Compensates for volume loss from aggressive filtering |

### Variations

**Pocket Game Boy / GBC feel** — slightly cleaner output:
```bash
python bitcrush.py song.mp3 -sr 22050 -bd 6 -lp 8000 -ws 0.4 -n
```

**Extreme DMG lo-fi** — the harshest, most authentic crunch:
```bash
python bitcrush.py song.mp3 -sr 8000 -bd 3 -lp 4000 -ws 0.85 -n
```

**Higher-pitched Game Boy jingle** — pitch shift up for that tiny speaker feel:
```bash
python bitcrush.py song.mp3 -sr 11025 -bd 4 -lp 5500 -ps 1.3 -ws 0.65 -n
```

### How the pipeline creates the Game Boy sound

```
Input audio (44100 Hz, 16-bit stereo)
    │
    ▼ Pitch shift (optional)
    │  Shifts frequency content up/down before any degradation
    │
    ▼ Low-pass filter @ 5500 Hz
    │  Cuts the high frequencies the Game Boy speaker couldn't reproduce
    │
    ▼ Downsample to 11025 Hz
    │  Reduces sample rate to match Game Boy hardware
    │
    ▼ Bit crush to 4-bit (16 quantization levels)
    │  Creates the stepped, gritty waveform of 4-bit audio
    │
    ▼ Wave shaping @ 0.65
    │  Pushes the waveform toward a square wave (pulse wave synthesis)
    │
    ▼ Normalize
       Final volume compensation
```

## Processing Pipeline Reference

The stages always run in this order:

1. **Pitch Shift** — FFT-based resampling to change pitch without altering duration
2. **Low-Pass Filter** — 5th-order Butterworth, removes high frequencies and acts as an anti-aliasing filter before downsampling
3. **Downsample** — Polyphase resampling (`resample_poly`) from original to target sample rate
4. **Bit Crush** — Quantizes the signal to `2^bit_depth` levels
5. **Wave Shaping** — Blends tanh soft-clipping with hard square-wave clipping
6. **Normalize** — Scales peak to 0.95 to prevent clipping
