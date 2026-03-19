## Short: "hashcat in 60 Seconds"

---

## Headline
One Tool, 300 Hashes

## Text

This is hashcat. The world's fastest password recovery tool.

Install it in one command. Feed it a hash. Pick an attack mode. Watch it work.

Dictionary attack — throw a wordlist at it. Brute force — try every combination. Rule-based — mutate passwords intelligently. Hashcat does it all.

And here's the thing — scroll through the supported hash types. MD5, SHA-256, bcrypt, WPA, zip files, Office documents...

Over 300 hash types. One tool. Every platform.

If a hash exists, hashcat probably cracks it.

One tool. 300+ hash types. Now you know.

---

## Display / CLI / Code

```bash
# Install
apt install hashcat

# Scroll through supported hash types
hashcat --help | head -60

# Count the number of supported hash modes
hashcat --help | grep -c "^[[:space:]]*[0-9]"

# Run a quick dictionary attack against an MD5 hash
echo "5f4dcc3b5aa765d61d8327deb882cf99" > hash.txt
hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

Show output:
- `--help` scrolling fast through hundreds of hash type entries
- grep count returning 300+
- hashcat cracking "password" from rockyou.txt in under a second
