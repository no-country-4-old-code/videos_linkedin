## Text

With `strings` I can extract strings which are stored inside a binary.
Sure, I would see the same strings with `cat`, but `strings` already filters out all the binary garbage.

If you have installed binutils already, then you already have `strings` on your system.
Otherwise, just install it with:
`sudo apt install binutils`

Now we need something to analyse.
Let's start with the APK for Signal: `Signal-Android-website-prod-universal-release-8.3.4.apk`

After downloading, I have to unzip it first:
`unzip Signal-Android-website-prod-universal-release-8.3.4.apk -d signal/`
The `-d` option specifies the output directory.

The result looks like this:
`ls -la signal/`
You can see the icons, resources, etc. here.
We will focus on the executable binary inside.

`strings signal/lib/x86_64/libsignal-client.so`
With the `-n` option I set a minimum length. So with `-n 6` I only see strings which are at least 6 characters.
Default length is 4.

`strings -n 6 signal/lib/x86_64/libsignal-client.so`

Now we pipe the output to `grep`. With `-i` the match is case-insensitive:
`strings signal/lib/x86_64/libsignal-client.so | grep -i http`
Then we pipe it further to `sort -u`, which makes sure we only see unique entries.
And then we pipe it to `less` to browse it from top to bottom and not pollute our shell:
`strings -n 6 signal/lib/x86_64/libsignal-client.so | grep -i http | sort -u | less`

Here we see a lot of hardcoded URLs, which are very likely endpoints.
You can see that Signal communicates directly to Giphy (I made a short video about this one),
you also see that Signal uses Stripe, here we see a link to post-quantum crypto.. etc.

I mostly control my search with `grep`.
I can e.g. grep for lines which fulfill password requirements, or for lines which contain common usernames.
Let's grep for email addresses using an extended regex with `-E`:
`strings -n 6 signal/lib/x86_64/libsignal-client.so | grep -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'`

One last thing I want to show you is the `-t x` option.
Here we see the offset of the found string inside the binary.
`strings -t x firmware-update-v4.2 | grep -Ff common_user_names.txt`
If I want to see what is stored near this location, I just copy the offset.
Then I open a hex editor of my choice and look around that location.
Here I use `xxd`. With `-s` I specify the offset and with `-l` I specify the number of bytes I want to see:
`xxd -s 0x814d -l 0x40 firmware-update-v4.2`

If you liked this quick `strings` tutorial, give it a like.
Thanks for watching, and have a nice day.
