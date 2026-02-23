## Code
- No salt => Password -> hash(Password) -> 12341
- With Salt => Password -> hash(Password + SaltValue) -> 123124

- Show multiple tables
--> qwert, 1234567 , with different SALT values 

## Text

> Welcome,
> Today we’re talking about rainbows and salt.

> Let’s start by putting ourselves in the shoes of a password cracker.
> Cracking a password hash can take a very long time depending on the hash function.
> Trying every password from a 14-million-entry list like the RockYou leak can take many hours if the function is intentionally slow (for example scrypt).

> So why not save time by precomputing the hashes for all those passwords once and storing them in a big table ?
> The next time we need to crack a hash, we can just look the hash up and get the matching password instantly — or at least quickly learn that the password isn’t in the list.
> Such a precomputed lookup is called a rainbow table.

> The good news for developers is that you can defend against rainbow tables by salting your hashes.
> Instead of storing or comparing hashes of plain passwords, your application hashes the password together with a salt value.
A salt is some additional data combined with the password before hashing.
The salt value does not need to be secret, but it should be unique.
With salt, same password create different hashes if their salt value is different.

So an attacker with a prebuilt rainbow table cannot use it unless the table was built using the exact same salt value.
> If you go one step further and ensure that each of your users, devices, or other entities gets its own unique, randomly generated salt, 
> then you make rainbow-table attacks against your application very impractical.

And that’s it for today!  
If you found this video helpful, give it a like and follow for more.  
See you next time!

(
But this raises another question:
Is this maintainable ? Now we have besides a password, a salt value for everything.
Well, it depends.
I personally would strongly tend to yes, because the salt value does not need to be a secret.
It can be shared like other non-sensitive information.
But please, feel free to share your oppinion regarding this in the comments below.
Until next time, bye.
)
