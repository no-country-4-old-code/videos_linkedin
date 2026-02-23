## Environment
- WSL Ubuntu 22 LTE
- Windows

## TEXT

Hi everyone,
here is why you should **not** store your passwords as clear text in your application or firmware.

When I say **"clear text"**, I mean storing passwords directly like this.

If an attacker gains access to your binary—whether through a leaked firmware update, by extracting it from a manipulated device, or by any other means—then the password can easily be read out.

For example, the tool **`strings`** (which comes with the installation of *binutils*) can be used to print all readable strings within a binary.
Let’s combine it with some filtering:
Here I use the `-n` parameter to set the minimum string length to 8.
Then I use `grep` to print only lines which contain at least one number, one uppercase letter, one lowercase letter, and one special character.
And — *voilà* — here is our password.

Another approach would be to search for common usernames.
This is based on the assumption that the username and password are located close to each other in the binary.

But if you find that this looks way too hacky… well, you could also just open the binary in the Windows text editor and scroll through it for a while.
Then you will also find the Password.

BECAUSE anyone can read a password which is stored in clear text.
So storing a Password in clear text is a Pretty dumb idea.
A much better alternative is to store a **salted hash** of the password instead.
The hash may still be extracted, but the attacker then needs to **crack** it to retrieve the real password.

And that’s it for now.
If you liked this video, don’t forget to leave a like, and I hope to see you next time.
Bye.

## CLI
"my_password"

sudo apt install binutils
strings -n 8 firmware-update-v4.2 |
        grep -P '^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[_\W]).+$'.

strings firmware-update-v4.2 -t x | grep -Ff common_user_names.txt
xxd -s 0x814d -l 0x40 firmware-update-v4.2xx

Windows Editor -> "Search for Password"
