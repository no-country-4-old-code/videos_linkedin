## Short: "What rockyou.txt Says About Humans"

## REVIEW:
Overwork completly.
A short about leaked passwords is fine.
Something like "leaked", "passwords", "free for everyone" .. should be in the first seconds as hook.
Short mention about RockYou (famous one).
Then mention newer wordlists in github. "It does not stop here... X, Y, Z.. there are coming new passwords lists in all the time.".
And the cover at least all those cheap password you can imagine. (Showing qwerty, password123..).
So Password complexity is really a thing.

---

## Headline
14 Million Bad Passwords

## Text

rockyou.txt. 14 million real passwords leaked from a 2009 data breach.

It's the default wordlist for every password cracking tool. Including hashcat.

Open it. The top password is "123456". Followed by "12345". Then "password". Then "iloveyou".

Run a quick analysis — over 40% of all passwords are under 8 characters. More than a million people used their own name. Tens of thousands used "letmein" or "qwerty".

This file isn't just a wordlist. It's a study in human psychology.

People are predictable. And attackers know it.

---

## Display / CLI / Code

```bash
# Get rockyou.txt if not present
ls /usr/share/wordlists/rockyou.txt

# How many passwords?
wc -l /usr/share/wordlists/rockyou.txt

# Top 10 most common
head -10 /usr/share/wordlists/rockyou.txt

# How many are under 8 characters?
awk 'length < 8' /usr/share/wordlists/rockyou.txt | wc -l

# How many contain "love"?
grep -i "love" /usr/share/wordlists/rockyou.txt | wc -l

# How many are purely numeric?
grep -c "^[0-9]*$" /usr/share/wordlists/rockyou.txt
```

Show output:
- `head` revealing "123456", "12345", "password", "iloveyou" — pause for effect
- Short/numeric password counts that feel embarrassingly high
- "love" count in the hundreds of thousands — human angle lands here
