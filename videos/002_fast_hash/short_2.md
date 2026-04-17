## Short: "MD5 Was Never Meant for Passwords"

---

## Headline
MD5 Was Too Fast

## Text

MD5 was built for file integrity checks — verifying downloads, detecting corruption. Speed was the whole point. You want checksums to be instant.

But then developers started hashing passwords with it. And suddenly, that speed became a vulnerability.

When we run a benchmark test, we see that hashcat checks nearly 1 billion MD5 hashes per second - even without GPU support.

MD5 was designed to be fast.
That's the problem.

But thank god, there are Key Derivation Functions.
KDFs were designed to be ugly.
That means they are memory hungry, slow, hard to optimize or parallelize.
Look how the benchmark drops down from 1 billion to only 200 hashes per second when we use a KDF like scrypt for hashing our passwords.

Beautifully slow.

---

## Display / CLI / Code

```bash
rm  ~/.local/share/hashcat/hashcat.potfile

# Intended use: file integrity check (fast is good here)
md5sum ubuntu-24.04-desktop-amd64.iso

# Show misuse: Create password hash with md5sum
echo -n "newBegin#046" | md5sum
hashcat -m 0 -a 0 61930f968724ee415f7f365693f0e8d5 rockyou*

# Misuse: cracking passwords at full MD5 speed
hashcat -b -m 0
man hashcat 
/scrypt
hashcat -b -m 4110
```

Show output:
- `md5sum` returning instantly with a checksum — looks innocent, useful
- `hashcat -b -m 0` showing ~1,000,000,000 H/s — same algorithm, terrifying context
- Contrast the two side by side
