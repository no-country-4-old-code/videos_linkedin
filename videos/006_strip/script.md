## Title
TOP 3 REASON WHY YOU SHOULD STRIP YOUR BINARIES

## Code
gcc main.c -O3 -o main
file main
nm main

rustc -C opt-level=3 main.rs -o -main_r
file main_r
nm main_r

./main
strip main
./main

stat -c %s main_rust
strip main_rust
stat -c %s main_rust

./secured_app
..Miau -> Denied
file secured_app
nm secured_app
gdb secured_app
gdb break check_password
gdb run
gdb disass
// mark ifeq
gdb b *0x12312
gdb c
gdb disass
gdb ni
gdb disass
gdb set $rip=0xdkdkkd
gdb c



## Text
> Welcome everyone, 
> today we'll talk about why you should strip your binaries. 

> But first things first: 
> During the build process, your binary gets enriched with meta-information, including symbols for static linking. 
> After linking, these symbols aren’t needed anymore. 
> But if you don’t strip them explicitly, they stay in your binary—even in optimized builds.

> Here are my TOP 3 reasons why you should remove them for your release builds:

Reason No. 1
As I already mentioned, you do not need them anymore — the party is over. Static linking is done, so stripping them does no harm.

Reason No. 2
Symbols take space. Depending on your code size, this can be significant. Rust binaries include debug symbols by default, so this example is a little exaggerated... but you get the idea.

Reason No. 3
Symbols leak information to attackers and help them understand how your system works. 
Here’s a simple example: 
the attacker does not know the passwor, but recognize that 
The attacker looks in the symbols, then sees the check_password function (and is very happy). 
He or she starts the program with the GNU Debugger.
 The debugger complains because there are no debug symbols... but we have static symbols, so setting a breakpoint is very convenient. 
Then run, enter a wrong password, continue and disassemble; 
observe which branch of the ifeq statement is taken when the wrong password is entered, and then switch branches by setting the instruction pointer directly.

And that’s it for today.
Did I forgot something or oversimplified things ?
Let me know in the comments.
Peace and out.
