## Text

With `strings` I can extract strings which are stored inside a binary.
Sure, I would see the same strings with `cat`, but `strings` already filters out all the binary garbage.

If you have installed binutils already, then you already have `strings` on your system.
Otherwise, just install it with:
`sudo apt install binutils`

Now we need something to analyse.
Let's start with the APK for Signal: `Signal-Android-website-prod-universal-release-8.3.4.apk`

I unzip it with -p and pipe the output to strings.

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

A lot of recent attacks injected malware in apps by compromising the github repsoitoris they use.
*add just a " | grep github/" at the end*
Signal for e.g. uses this github-Repo here, with a lot of contributers.

As you can see, I mostly control my search with `grep`.
I can e.g. grep for email addresses, grep for lines which fulfill password requirements, or for lines which contain common usernames.
But given the fact that this is not grep tutorial, lets skip that and focus on "strings" again.

One last thing I want to show you is the `-t x` option.
I prepared a little example file for this.
Here we see the offset of the found string inside the binary.
`strings -t x firmware-update-v4.2 | grep -Ff common_user_names.txt`
If I want to see what is stored near this location, I just copy the offset.
Then I open a hex editor of my choice and look around that location.
Here I use `xxd`. With `-s` I specify the offset and with `-l` I specify the number of bytes I want to see:
`xxd -s 0x814d -l 0x40 firmware-update-v4.2`

If you liked this quick `strings` tutorial, give it a like.
Thanks for watching, and have a nice day.
