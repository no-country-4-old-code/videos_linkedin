## Short: "Know What's Coming at Your Hashes"

---

## Headline
Know Your Enemy's Tools

## Text

If your password database leaks, here's exactly what hits it next.

A hash is one-way — there's no reverse. So attackers try passwords until one matches. Hashcat automates that at scale.

Hashcat supports Brute-force, which is just trying out every possible combination.
and Dictionary attacks.
Here you pass hashcat a list of often used passwords to check.

All passwords which hashcat should test, can be mutated by so called rules.
This way "password" becomes "P@assw0rd".

Depending on our hash-function, hashcat can run billions of attempts per second.
This speeds up with Potfile caching.
Every hash which is cracked before is instant resolved — no recomputation.

Defend against it by using Key-Derivatve-Function for hashing and enforce a minimal password complexity.


---

## Display / CLI / Code

---

## Display / CLI / Code

```bash
# Create a test hash (MD5 of "password")
echo -n "password" | md5sum
# => 5f4dcc3b5aa765d61d8327deb882cf99

# Create a list : leaked_hashed_pwds.txt
Show List 

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
