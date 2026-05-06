## Short: "Cracking VeraCrypt Starts With the Header"

---

## Headline
Crack VeraCrypt In Two Steps

## Text

Cracking your encrypted disk might be easier then you think.
Encrypted disk? Cool. If your password is weak, the whole thing comes off in two steps.

Step one: get the volume header. The first 512 kilobytes of a VeraCrypt container hold a key derivation blob — that's the only part the cracker actually needs. John the Ripper ships a tool called veracrypt2john.py. Point it at the volume, redirect to a hash file. Done.

Step two: feed it to hashcat in mode 13721 — that's PBKDF2-SHA-512 with AES-XTS, the default VeraCrypt volume. Add rockyou.txt. If the password's in the list, the volume key falls out.

What saves you? VeraCrypt's KDF is already slow on purpose, so the only thing left is your password. Make it long, random, and not in any list.

Lab demo only — your own volume, your own password. Next short: WiFi. See you then.

---

## Display / CLI / Code

```bash
# Clean potfile so the demo output is predictable
rm -f ~/.local/share/hashcat/hashcat.potfile

# Step 1 — extract the VeraCrypt header into a hashcat-compatible hash
# veracrypt2john.py ships with John the Ripper (/usr/share/john/ on Kali/Ubuntu)
python3 /usr/share/john/veracrypt2john.py secret.hc > vc.hash

# Inspect — one line starting with $veracrypt$...
head -c 120 vc.hash ; echo

# Step 2 — hashcat mode 13721 = VeraCrypt PBKDF2-HMAC-SHA512 + XTS (default volume)
hashcat -m 13721 -a 0 vc.hash /usr/share/wordlists/rockyou.txt

# Reveal the cracked password
hashcat -m 13721 vc.hash --show
```

Show: `veracrypt2john.py` printing one opaque hash line → `hashcat` cracking status spinning → `--show` printing the cleartext password. Pause on the recovered password.

---

## Youtube title
1. Cracking a VeraCrypt Volume in Two Steps
2. Your VeraCrypt Disk Falls in 2 Commands If Your Password Is in rockyou.txt
3. veracrypt2john + hashcat -m 13721: The Full Volume-Cracking Pipeline
4. Is VeraCrypt Actually Safe If You Pick a Bad Password?

## Youtube Description
Encrypted volumes are only as strong as their passwords. This short shows the two-step attack on a VeraCrypt container: extract the volume header with `veracrypt2john.py` from John the Ripper, then crack the resulting hash with hashcat in mode 13721 (PBKDF2-HMAC-SHA-512 + AES-XTS) using the rockyou wordlist. Lab demo against a volume we own.

Commands shown:
- `python3 /usr/share/john/veracrypt2john.py secret.hc > vc.hash`
- `hashcat -m 13721 -a 0 vc.hash /usr/share/wordlists/rockyou.txt`
- `hashcat -m 13721 vc.hash --show`

#infosec #veracrypt #hashcat #diskencryption #cybersecurity

## LinkedIn Description
Full-disk and container encryption with VeraCrypt is sound — until the user picks a password from any public wordlist; the KDF is slow, but slow doesn't help against a list it finds in minutes. Enforce 16+ character passphrases for high-value volumes and consider hardware tokens for anything that really needs to stay sealed.

#blueteam #encryption #cybersecurity
