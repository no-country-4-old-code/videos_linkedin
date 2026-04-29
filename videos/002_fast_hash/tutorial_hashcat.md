## Text

If you want to "xyzyz" hashes, you should try out hashcat.
It supports less hash-algorithmus then "JohnTheRipper" - another great tool -, but it is faster.

Installation is straight-forward for debian based systems (sudo apt get install hashcat).

Lets create a password-hash with MD5. 
I use the "-n" option here to prevent "echo" from adding a "\n" at the end.. which would polute our hash.
BTW: Never use fast hash-functions like MD5 for hashing passwords. Use KDF like argon or scrypt.
I just use it here because I want cracking to be fast.

Now there a different approach to restore the password  this hash.
The most inefficient is brute force.
hashcat -a 3 -m 0 ?L?l?l?l?
-a defines the attack type "3" stands for brute force.
-m defines the hash type. "0" stands for MD5.
And those question marks behind it are a mask with alias for the password.
You an loock up those in the man page.
"man hashcat" "/?l" .. 
*Explain ?L?l..*
*going  back* With this command, hashcat generate a MD5 Hash for every possible combination of a Any Big Letter word, followed by 4 low letter words.
If we do not know, how many letters the password has, and which charakters are used, we could do something like this.
hashcat -a 3 -m 0 --all ?a?a?a?a?a?a?a?a
"--all" start with testing every 1-charakter-word-combination, then every 2-charakter-word-comn, then every 3.. etc.
The ?a alias stands for every letter.
Image that hashcat supports around 90 different charakters, there are 90**n possible passwords for a n-charakter long password. This becomes very fast not feasible. This outruns the perfomrance of your maschine very fast.

The default appraoch of hashcat to crack passwords is the dictonary attack.
For this you give hashcat a list of potential passwords.
The most famous list of passwords are the "rockyou.txt" files.
nvim rockyou.txt 
The name comes from a company which saves they passwords of their users in cleartext.
And there was a database breach.. so yeah.. now the world has a good impresison of passwords.
wc -l rockyou* 
They contain xxx potential passwords, but if you look deeper there are also a lot of garbage in it..

Anyway.. with this command "hashcat -a 0 -m 0 12313151 /rockyou" 
hashcat calculates the hash of every of those passwords passed with the second parameter, and compare it with the hash to crack (first parameter).

Which works fine.

Instead of passing a single hash, you could also pass a list of hashes as first parameter for simulatan cracking.
nvim leaked.txt
hashcat -a 0 -m 0 leaked.txt /rockyou

If you ran a command twice, you see that their is no calculation needed anymore.
Thats because every password-hash which was scucessfuly cracked by hashcat once, is cached in its potfile to speed up.
You can see the content of the potfile by "hashcat --show ...

So this .potfile is technically your personal rainbow table for already cracked passwords.
If a user uses a password covered by your table and hashed with MD5, then cracking is done in no time.
echo -n "ajajaj" | md5sum
hashcat -a 0 -m 0 dkdkdkddkdk /rockyou..

A defend-technique against rainbow tables is salting.
So after you user entered his password, you add to this string another one. E.g this one here.
This additonal string is called "salt".. and it does not need to be secret in anyway.
The effect is, that it changed the hash.
Which means our little rainbow-table, aka. potfile , it not working anymore.

hashcat can deal with salted hashes.
hashcat -a 0 -m 0 --salt qweqe mdmdmdmdmd /rockyou .
With "--salt" we pass the salt vaule to hashcat. Hashcat now internall extend every password in rockyou with the salt value. So the salt just forced hashcat into recalclation.

There is one major puzzle piece of hashcat that you need to know - rules.
What if someone uses a password from your list e.g. password123 ,
but modified it via leetspeech "p4ssw0rd123" or count it up ?
It is not longer contained in your password list, so it wont be found.

hashcat covers those cases with rules.
hashcat --stdout -d password /lllll 
I use the stdout option to just see he output. This is no cracking, its just testing.
I can write my own rules, but here I used the leetspeak-rule which was shipped with hashcat.
With rules I can automatically cover an infinte amount of variation of a password.

I can use it directly in a dictonary attack:
hashcat -a 0 -m 0 --kkdkdkddk

But hashcat is not only about cracking.
It is alos about building wordlists.. for cracking or other things.
And here comes everyhing together.

E.g. an attacker would analyse a webpage and extract a few keywords.
Short list.
Password might be a combination of those words, lets use
hashcat -a 4 ..
to create a combined wordlist.
Or wait.. we are not sure, if both words are just matched together.
Lets create a rule to add a suffix to words in one list first.
Now merge again..
Now lets say, we want a increasing number at the end, because this is the way people deal with "please change your password" issues. 
We use rules for that and the "?a" aliases we know from the brute force attack.
Now this is our password lists, which we can use in our dictonary attack.
BAMM..

At the end of this video, lets take a look at the performance.
How many hashes can hascat try out per second.

hashcat -b -m 0 
And we see that hashcat try out over 1 billion hashes per second..in case of MD5.

What if someone hashes their password with a Key-deriviation-function like scrypt. (Sadly Argon2).
man hashcat
/scrypt
hashcat -b -m 8900
And we see that the number of attempts per second drops to 200, which is around 20 millions slower.
So.. thats the reason why you should hash your passwords with KDF.

But coming back to MD5.
hashcat utilies per default the GPU as long as there is a driver for it.
Hashcat -kkkk

And thats it.
Got longer as expected, but.. at least now you have an idea.










