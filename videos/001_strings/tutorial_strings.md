## Text

With "strings" I can extract strings which are stored inside a binary.
Sure, I would see the same "strings" with cat, but "strings" already filltered out all this bullshit here.

If you have installed binutils already, then you already have "strings" on your system.
Otherwise, just type ".." on debian based systems.

Now we need something to analyse.
Lets start with the APK for Signal.

After downloading, I have to unzip it first with "unzip -xyz1234".
"short explanation of options".

The result looks like this "ll". You see the icons etc. here.
We will focus on the later executable binary , "strings ..."
With the "-n" Option , I set a minimum length. So with -n 6 , I only see strings which are at least 6 charakters.
Default length is 4.

Now we pipe the output to grep. With -i ... *explain operators here*.
The we pipe it further to "sort" which makes sure we only see unique entries with the -u option.
And then I pipe it to "less" to browse to it from top to bottom and not polute our bash.

Here we see a lot of hardcoded URLs, which are very likly endpoint.
You see that Signal commuicates direct to giphy (I made a short video about this one),
you also see that Signal uses Stripe, Here we see a link to post-crypto.. etc.

I mostly control my search with grep.
I can e.g. grep for lines, which fullfill password-requirments or for lines which contain common usernames.
Lets grep for email addresses, I use "xyz.." here. *explain grep options*

On last thing I want you to show, is the "-t x" option.
Here we see the offset of the found string inside the binary.
If I want to see what is stored near this location, I just copy the offset.
THen I open a hexeditor of my choice and look around this location.
Here I use xxd, with -s , I specify the offset and with -l I specify the number of bytes I want to so.

If you liked this quick "strings" tutorial, give it a like.
Thanks for watching, and have a nice day,












- Motivation
- 
