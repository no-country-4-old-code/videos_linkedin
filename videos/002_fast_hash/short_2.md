## Short: "MD5 Was Never Meant for Passwords"

---

## Text

MD5 was designed to be fast. That's the problem.

It was built for file integrity checks — verifying downloads, detecting corruption. Speed was the whole point. You want checksums to be instant.

But then developers started hashing passwords with it. And suddenly, that speed became a vulnerability.

Watch this. MD5 on a file — milliseconds, exactly as intended.

Now watch hashcat run MD5 as a password cracker. One billion hashes per second.

That's not a bug. That's MD5 working exactly as designed.

Using MD5 for passwords is like using a race car as a speed bump.

---

## Display / CLI / Code

```bash
# Intended use: file integrity check (fast is good here)
md5sum ubuntu-24.04-desktop-amd64.iso

# Misuse: cracking passwords at full MD5 speed
hashcat -b -m 0
```

Show output:
- `md5sum` returning instantly with a checksum — looks innocent, useful
- `hashcat -b -m 0` showing ~1,000,000,000 H/s — same algorithm, terrifying context
- Contrast the two side by side
