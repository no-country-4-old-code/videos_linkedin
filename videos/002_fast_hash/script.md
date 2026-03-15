## Title
Fast, faster, unsecure !
(rocket as symbol)

## Text
Faster is always better, right ?
Well..it depends... at least in case of cybersecurity.
If you hash your password using the fast MD5-hash-function,
then attackers benefit massive from that.

Cracking tools.. sry, I meant "password recovery utilities" like hashcat need to calculate the hashes of billions of potential passwords.
..and when calculating hashs is fast, then cracking them, is it also.

Lets make a benchmark test with hashcat on an average PC and without GPU support.
-b stands for benchmark. -m specifys the identifer of the hashfunction , which is 0 for MD5...
And the result is solid.. hashcat can check around 1 billion MD5 hashes per secound.

So you do not want a fancy hash function for hashing passwords; you want a ugly one.
And Key-derivation functions like Argon2 or scrypt are very ugly by design.
Slow, memory hungry and hard to optimize.
Nothing you want to run in a loop..

Lets run the benchmark test again for scrypt.
Hashcat performance on the same system drops down to 200 hashes per second when using scrypt.
So, by choosing a KDF for hashing, you really slow down attackers.

And thats it for today,
next time we talk about rainbow-tables and how salt destorys them.
Cerioo

## Code / Display

- Github of hashcat: https://github.com/hashcat/hashcat
- hashcat -b -m 0  ==> run + result
- man hashcat ; scrolling down to /scrypt 
- hashcat -b -m 4110 ==> run + result





