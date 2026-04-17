## Short: "How Passwords Actually Get Cracked"

---

## Headline
Try Every Password

## Text

A hash is a one-way function. There's no reverse. The only way to crack it is to try passwords until one matches.

That's not a clever insight — that's the entire attack.

And hashcat is the tool that automates it at scale.

Dictionary attack: feed it a wordlist, it hashes each word and checks for a match. Brute-force: try every possible combination. Rule-based: mutate words intelligently — "password" becomes "P@ssw0rd". Hybrid modes combine wordlists with masks.

GPU support makes all of this billions of times faster. And potfile caching means a hash you've cracked once? Never cracked again — it's stored.

A lot of supported hash types. MD5, SHA, bcrypt, WPA, Office documents — if it's hashed, hashcat handles it.

---

## Display / CLI / Code

```bash
# Create a test hash (MD5 of "password")
echo -n "password" | md5sum
# => 5f4dcc3b5aa765d61d8327deb882cf99

# Dictionary attack against that hash
echo "5f4dcc3b5aa765d61d8327deb882cf99" > hash.txt
hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt

# Brute-force: 4-character lowercase passwords
hashcat -m 0 -a 3 hash.txt ?l?l?l?l

# Already cracked? Potfile remembers — show cached result
hashcat -m 0 hash.txt --show

# Count supported hash types
hashcat --help | grep -c "^\s*[0-9]* |"
```

Show output:
- Dictionary attack cracking "password" instantly from rockyou.txt
- `--show` returning the result without re-running — potfile in action
- Hash type count printing ~500
