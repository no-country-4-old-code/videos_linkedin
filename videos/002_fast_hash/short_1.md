## Short: "Know What's Coming at Your Hashes"

---

## Headline
Hashcat Eats Your Hashes

## Text

If your password database leaks, here's exactly what hits it next.

A hash is one-way — there's no reverse. So attackers try passwords until one matches. Hashcat automates that at scale.

It supports brute-force — trying every possible combination — and dictionary attacks, where you feed hashcat a list of commonly used passwords.

Every candidate can be mutated by so-called rules. This way "password" becomes "P@ssw0rd".
Take this leetspeak.

Depending on the hash function, hashcat runs billions of attempts per second. Potfile caching pushes it further: every hash cracked before is resolved instantly — no recomputation.

Defend with a Key Derivation Function, a minimum password complexity, and salted hashes — the last one kills rainbow tables.

---

## Display / CLI / Code

```bash
# Create a test hash (MD5 of "password")
echo -n "password" | md5sum
# => 5f4dcc3b5aa765d61d8327deb882cf99

# Save the leaked hash to a file
echo "5f4dcc3b5aa765d61d8327deb882cf99" > hash.txt
Generate a leaked_hashes.txt with md5sum hashes by running md5sum on a random sample of 50 passwords from rockyou.txt .

Show the CLI with the leaked.txt . (ls)
Open it and show the hashes.

hashcat (not executed)
hashcat ---brute force attack (not executed) :  hashcat -m 0 -a 3 leaked.txt ?a?a?a?a?a?a
hashcat ---dictonary attack (not executed) : hashcat -m 0 -a 0 leaked.txt rockyou.txt
hashcat --- password -> leetspeak rule (executed) : echo "icebox_quantum_eagles" | hashcat --stdout -r /usr/share/hashcat/rules/leetspeak.rule 
hashcat --- show potfile caching (executede) : hashcat -m 0 hash.txt --show

# Dictionary attack using the rockyou wordlist
hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt

# Brute-force: 4-character lowercase passwords

# Already cracked? Potfile remembers — instant result

# Count supported hash types
hashcat --help | grep -cE "^\s*[0-9]+ \|"
```

Show output:
- Dictionary attack cracking "password" instantly from rockyou.txt
- `--show` returning the result without re-running — potfile in action
- Hash type count printing ~500
