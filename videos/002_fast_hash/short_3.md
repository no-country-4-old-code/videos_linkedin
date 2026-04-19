## Short: "Your GPU Is a Password Cracking Machine"

---

## Headline
Cracking Passwords: GPU Is Default

## Text

Utilizing a GPU isn't an advanced technique — it's the default.

In tools like Hashcat, GPU cracking is on by default. Attackers would have to manually disable it, using the -D flag.

But why would they?

Even my mediocre laptop GPU gives a 4x speedup on MD5 — from 500 million to 2 billion hashes per second.

Switch to scrypt, and the GPU barely matters: 100 hashes per second versus 2 billion. That's 20 million times slower.

So let your attackers suffer by hashing your passwords with a key derivation function.
And don't assume any attacker is leaving performance on the table.

---

## Display / CLI / Code


```bash
# CPU-only benchmark
hashcat -b -m 0 --force --opencl-device-types 1

# GPU benchmark (default)
hashcat -b -m 0

# scrypt benchmark — absolute gap stays enormous
hashcat -b -m 4110
```

Show output:
- CPU-only MD5: ~500 MH/s
- GPU MD5: ~2,000 MH/s (~4x jump — modest, but the attacker already has this)
- scrypt on GPU: ~100 H/s (still 20,000,000x slower than MD5 on the same GPU)
- Highlight the absolute gap, not the proportional one
