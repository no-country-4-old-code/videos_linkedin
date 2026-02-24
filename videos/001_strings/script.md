## Environment
- WSL Ubuntu 22 LTE
- Windows

## TEXT

Everytime I see someone using cleartext password - direct or indirect - it gives me bad vibes.
Its like.. "Hey, lets deploy the password directly to the customer"
Even your grandma could open this file here with the way-to-boring windows text editor to read out the password.
Something YOUR grandma of course would NEVER do.
Because she is a damn professional. She would use a better tool for that - like strings. 
Here we see her using it with the -n parameter to extract only strings from the binary which have a minimum lentgh of 8.
Then she pipes the whole stuff to `grep` to print only only lines which contain at least one number, one uppercase letter, one lowercase letter, and one special character.
Which are the basic password requirments.. because nobody really wants to read through all the strings of a binary.
Our time on this planet is still limited, you know.

And sometimes when your grandma feels lucky, she prefers a more indirect method, by searching not for the password, but for common usernames instead.
With the -t option she gets the location of the string within the binary.
And then she just look a little bit around this location using a standard hex-editor..
..and.. ups.. find a password.
which of course only works if username and password are located close to each other in the binary, but well..
I am not here to tell you how to organize your code.

I am here to tell you to protect your passwords against evil grandmothers by hashing them.
The passwords of course..not the grandmothers.
And this hashing should be done with Key-derivate-Function and so on, because every evil grandma has a hashcat at home, which just wait to crack your hashes - but this will be the topic for next time.
So Stay safe until then, && like this video.. it my first one


## CLI
"my_password"

sudo apt install binutils
strings -n 8 firmware-update-v4.2 |
        grep -P '^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[_\W]).+$'.

strings firmware-update-v4.2 -t x | grep -Ff common_user_names.txt
xxd -s 0x814d -l 0x40 firmware-update-v4.2xx

Windows Editor -> "Search for Password"
