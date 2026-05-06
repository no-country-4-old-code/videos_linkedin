## Short: "What 14 Million Passwords Reveal About Humans"
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
14 Million Bad Habits

## Text

Fourteen million real passwords. Free download. And they tell you exactly how humans pick passwords.

rockyou.txt is the default wordlist for every password cracking tool. But forget the breach for a second — look at what's inside.

The first ten lines: 123456, 12345, 123456789, password, iloveyou. That's not the bottom of the list. That's the top.

The awk length distribution shows a third of the file is under 8 characters. About a quarter is pure digits. And tens of millions more leaked passwords keep appearing — HIBP, weakpass — same patterns, same humans.

If your password looks like anything we just scrolled past, a dictionary attack finds it before your coffee cools.

Check your own email at haveibeenpwned dot com. And next time, we extract a VeraCrypt header and feed it to hashcat. See you then.

---

## Display / CLI / Code

```bash
# File present and size
ls -lh /usr/share/wordlists/rockyou.txt
wc -l /usr/share/wordlists/rockyou.txt

# Top 10 — in frequency order
head -10 /usr/share/wordlists/rockyou.txt

# Length distribution — what does the actual spread look like?
awk '{ print length }' /usr/share/wordlists/rockyou.txt \
  | sort | uniq -c | sort -rn | head -12

# How many are digits only?
grep -cE '^[0-9]+$' /usr/share/wordlists/rockyou.txt

# How many are pure lowercase letters?
grep -cE '^[a-z]+$' /usr/share/wordlists/rockyou.txt

# The all-time favourites
grep -cwi 'qwerty\|password\|iloveyou\|letmein' /usr/share/wordlists/rockyou.txt
```

Show: `head` output pausing on the top-5 — let the embarrassment land. Length table: rows for 8, 7, 6 dominate. Digit-only and lowercase-only counts feel uncomfortably large. Classic-favourite count: still very much there.

---

## Youtube title
1. What 14 Million Real Passwords Tell You About Yourself
2. A Third of rockyou.txt Is Under 8 Characters — Here's the Full Breakdown
3. Reading rockyou.txt With awk and grep: A Pattern Tour
4. Why Does Every Password-Cracking Tool Start With the Same File?

## Youtube Description
A guided tour of what's actually inside `rockyou.txt` — the 14-million-password wordlist that ships with every cracking distro. We use `awk`, `sort`, `uniq`, and `grep` to look at length distribution, the share of digits-only and lowercase-only entries, and how often the obvious favourites still show up. The patterns repeat in every newer leak.

Commands shown:
- `wc -l /usr/share/wordlists/rockyou.txt`
- `head -10 /usr/share/wordlists/rockyou.txt`
- `awk '{print length}' /usr/share/wordlists/rockyou.txt | sort | uniq -c | sort -rn | head -12`
- `grep -cE '^[0-9]+$' /usr/share/wordlists/rockyou.txt`
- `grep -cE '^[a-z]+$' /usr/share/wordlists/rockyou.txt`

#infosec #passwords #rockyou #hashcat #cybersecurity

## LinkedIn Description
If your password policy still allows 8 characters with no complexity requirement, your users' choices are statistically indistinguishable from rockyou.txt — and any dictionary attack treats your hashes accordingly. Mandate 12+ characters with a deny-list seeded from public leaks, or move to passphrases.

#blueteam #passwordpolicy #cybersecurity
