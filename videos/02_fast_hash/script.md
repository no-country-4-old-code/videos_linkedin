## Text
> Hello everyone,

> Storing password hashes instead of passwords is a good idea.
> But not every hash function is suitable for hashing passwords.
MD5, for example, is a very fast hashing function.
"Fast" sounds good, but it means that cracking tools like Hashcat can check over a billion >hashes per second (even without GPU support).

> So you do not want a fast hash function for hashing passwords; you want a slow one.
> Key-derivation functions like Argon2 or scrypt are slow by design.

Here is a comparison:
Hashcat performance on the same system drops down to 200 hashes per second when using scrypt.
So, by choosing a KDF for hashing, you can really slow down attackers.

If you are unsure how fast your hash function is, I would advise you to run benchmark tests using Hashcat or John the Ripper.
For Hashcat, it is just `hashcat -b` for a benchmark and `-m` to specify the hash function.
A list of all supported hash functions can be found in the Hashcat manual.

That's all for today,
thank you.

## Code


