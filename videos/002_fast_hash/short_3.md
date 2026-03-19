## Short: "Your GPU Is a Password Cracking Machine"

---

## Headline
Your GPU Cracks Passwords

## Text

Your gaming GPU cracks passwords faster than most supercomputers from 10 years ago.

GPUs were built for parallel computation — thousands of cores doing simple math simultaneously. That's also exactly what hash cracking needs.

Run hashcat in CPU-only mode on MD5. Decent numbers. Now add the GPU. Watch the multiplier.

Billions of hashes per second. On consumer hardware.

But Key Derivation Functions like scrypt are memory-hard by design. They force sequential memory access — something GPUs are terrible at. The parallel advantage disappears.

That's not an accident. That's the defense.

That GPU isn't just for gaming anymore.

---

## Display / CLI / Code

```bash
# CPU-only benchmark
hashcat -b -m 0 --force --opencl-device-types 1

# GPU benchmark (default)
hashcat -b -m 0

# scrypt benchmark — GPU advantage collapses
hashcat -b -m 4110
```

Show output:
- CPU-only: ~100–200 MH/s
- GPU: ~1,000–10,000 MH/s (massive jump, hardware dependent)
- scrypt with GPU: ~200 H/s — basically the same as CPU
- Highlight the contrast: GPU wins on MD5, useless against scrypt
