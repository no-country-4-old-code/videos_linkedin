## Text

If you want to crack hashes, you should try out hashcat.
It supports fewer hash algorithms than JohnTheRipper — another great tool — but it is faster.

Installation is straightforward for Debian-based systems:
`sudo apt install hashcat`

Let's create a password hash with MD5.
I use the `-n` option here to prevent `echo` from adding a newline at the end, which would pollute our hash.
`echo -n "password" | md5sum`
BTW: Never use fast hash functions like MD5 for hashing passwords. Use a KDF like Argon2 or scrypt.
I just use it here because I want cracking to be fast.

There are several approaches to recover the password behind a hash.
The most inefficient is brute force.
`hashcat -a 3 -m 0 5f4dcc3b5aa765d61d8327deb882cf99 ?u?l?l?l?l?l?l?l`
`-a` defines the attack mode — `3` stands for brute force.
`-m` defines the hash type — `0` stands for MD5.
The question marks at the end are a mask describing the structure of the password.
You can look them up in the man page:
`man hashcat` then search `/?l`
*Explain ?u?l..*
*going back* With this command, hashcat generates an MD5 hash for every combination of one uppercase letter followed by seven lowercase letters, and compares each result against our target hash.
If we do not know how many letters the password has, or which characters are used, we can do something like this:
`hashcat -a 3 -m 0 --increment 5f4dcc3b5aa765d61d8327deb882cf99 ?a?a?a?a?a?a?a?a`
`--increment` starts by testing every 1-character combination, then every 2-character combination, then every 3-character one, and so on.
The `?a` alias stands for any printable character — letters, digits, symbols.
Imagine that hashcat supports around 95 different characters, so there are 95^n possible passwords for an n-character password. This becomes infeasible very fast. Brute force outruns the performance of your machine quickly.

The default approach of hashcat to crack passwords is the dictionary attack.
For this, you give hashcat a list of potential passwords.
The most famous password list is the `rockyou.txt` file.
`nvim rockyou_2025_00.txt`
The name comes from a company that stored its users' passwords in cleartext.
There was a database breach — so now the world has a good impression of what passwords people actually use.
`wc -l rockyou_2025_*.txt`
In total there are around 14 million potential passwords — but if you look closely, there is also a lot of garbage in it.

Anyway, with this command hashcat calculates the hash of every password in the list and compares it with the hash to crack:
`hashcat -a 0 -m 0 5f4dcc3b5aa765d61d8327deb882cf99 rockyou_2025_00.txt`
Which works fine.

Instead of passing a single hash, you can also pass a list of hashes as the first parameter for simultaneous cracking.
`nvim leaked.txt`
`hashcat -a 0 -m 0 leaked.txt rockyou_2025_00.txt`

If you run the command a second time, you'll see there is no calculation needed anymore.
That's because every password hash successfully cracked by hashcat once is cached in its potfile to speed things up.
You can see the content of the potfile by running:
`hashcat -m 0 --show leaked.txt`
The potfile lives at `~/.local/share/hashcat/hashcat.potfile`.

So the potfile is technically your personal rainbow table for already cracked passwords.
If a user uses a password covered by your table and hashed with MD5, cracking is done in no time.
`echo -n "password" | md5sum`
`hashcat -a 0 -m 0 5f4dcc3b5aa765d61d8327deb882cf99 rockyou_2025_00.txt`

A defensive technique against rainbow tables is salting.
So after your user enters a password, you append another string to it — for example this one here.
This additional string is called the "salt", and it does not need to be secret in any way.
The effect is that it changes the hash.
`echo -n "passwordNaCl" | md5sum`
Which means our potfile is not working anymore.

Hashcat can deal with salted hashes.
For salted MD5, we use hash mode 10 — that is `md5($pass.$salt)`.
The hash file needs to be in `hash:salt` format:
`echo "<hash from above>:NaCl" > hash_salted.txt`
`hashcat -a 0 -m 10 hash_salted.txt rockyou_2025_00.txt`
Hashcat now internally extends every password from the wordlist with the salt before hashing it. So the salt just forces hashcat into recalculation.

There is one major piece of hashcat that you need to know — rules.
What if someone uses a password from your list, like `password123`,
but modified it with leetspeak — `p4ssw0rd123` — or appends a digit?
It is no longer in your password list, so it won't be found.

Hashcat covers those cases with rules.
`echo "password" | hashcat --stdout -r /usr/share/hashcat/rules/leetspeak.rule`
I use the `--stdout` option to just see the output. This is not cracking, it's just testing.
I can write my own rules, but here I used the leetspeak rule shipped with hashcat.
With rules I can automatically cover an infinite amount of variations of a password.

I can use rules directly in a dictionary attack:
`hashcat -a 0 -m 0 5f4dcc3b5aa765d61d8327deb882cf99 rockyou_2025_00.txt -r /usr/share/hashcat/rules/best64.rule`

But hashcat is not only about cracking.
It is also about building wordlists — for cracking or other things.
And here everything comes together.

For example, an attacker would analyze a webpage and extract a few keywords.
Short list.
A password might be a combination of those words, so let's use the combinator attack:
`hashcat -a 1 --stdout keywords.txt keywords.txt > combined.txt`
Or wait — we are not sure if both words are just combined as-is.
Let's create a rule to append a suffix to words in one list first.
Now merge again.
Now let's say we want an incrementing number at the end, because that is how people deal with "please change your password" prompts.
We use a hybrid attack with `-a 6` — wordlist plus mask — where `?d` matches any digit:
`hashcat -a 6 --stdout combined.txt ?d?d?d > combined_plus.txt`
Now this is our password list, which we can use in our dictionary attack.
BAMM.

At the end of this video, let's take a look at performance.
How many hashes per second can hashcat try?

`hashcat -b -m 0`
And we see that hashcat tries over 1 billion hashes per second — in the case of MD5.

What if someone hashes their password with a Key Derivation Function like scrypt (hashcat sadly does not support Argon2 out of the box)?
`man hashcat`
`/scrypt`
`hashcat -b -m 8900`
And we see that the number of attempts per second drops to around 200, which is roughly 5 million times slower.
That's the reason why you should hash your passwords with a KDF.

But coming back to MD5.
Hashcat utilizes the GPU by default, as long as there is a driver for it.
`hashcat -I`

And that's it.
Ran longer than expected, but at least now you have an idea.
