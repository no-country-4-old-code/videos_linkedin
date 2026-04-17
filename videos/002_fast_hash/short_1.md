## Short: "Know What's Coming at Your Hashes"

---

## Headline
Know Your Enemy's Tools

## Text

If your password database leaks, here's exactly what hits it next.

A hash is one-way — there's no reverse. So attackers try passwords until one matches. Hashcat automates that at scale.

Dictionary attack: every word in a wordlist, hashed and compared. Brute-force: every possible combination. Rule-based: mutations — "password" becomes "P@ssw0rd". Hybrid modes combine all of the above.

GPU support makes this billions of attempts per second. Potfile caching means any hash cracked before is instant — no recomputation.

This is the tool testing your users' password choices right now. Know how it works. Choose your hashing algorithm accordingly.

---

## Display / CLI / Code

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
