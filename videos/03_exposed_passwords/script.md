## Show
// Prep
rm  ~/.local/share/hashcat/hashcat.potfile
echo -n "newBegin#046" | md5sum
// Prep ends

- Repository of Rock-You:
https://github.com/josuamarcelc/common-password-list.git

hashcat -m 0 -a 0 61930f968724ee415f7f365693f0e8d5 common-password-list/rockyou*
-> show cracked and password.

grep 1234 common-password-list/rockyou*
grep qwert common-password-list/rockyou*
grep p@55w0rd common-password-list/rockyou*

- Show https://haveibeenpwned.com/
(and enter my-email@gmail.com)

## Text
> Welcome to a new episode.  
> Today we talk about lists of leaked Passwords - or why you should not use the same Password over and over again.  

> So 	Imagine you create a user account on the webpage of a cool new startup.  
> A few months later, this startup gets hacked because it prioritized "time to market" over "cybersecurity."  
> From now on, your password is contained in some "common-password lists" around the internet.  

The most famous example of one of these lists is RockYou.txt.  
RockYou was a company that got hacked in 2009, which led to the exposure of around 14 million passwords.. which were stored in cleartext btw.  
The lists are hosted in this repository and also in multiple others.  

Now, every time someone tries to get access to an account or crack a hash, the first thing they do is throw the passwords from those leaked lists at it to see if it breaks.
Here I create a MD5 hash of a password.
(Which You should never do. I only use MD5 here for Performance reasons).
Then I try to crack it with a simple dictonary attack with hashcat.
When I hit enter, hashcat just creates a hash for every password in the rock-you-files and compare this hash to the to-be-cracked hash.
And it works.

Lists of leacked passwords are also the reason why you should not use oversimplified passwords—because those are definitely in one of these lists.
Here are some examples.

If you want to check whether your email address is in one of these data leaks, visit https://haveibeenpwned.com/.  

And that’s it for today!  
If you found this video helpful, give it a like and follow for more.  
See you next time!

