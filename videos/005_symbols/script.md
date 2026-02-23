## Title
What are symbols ? Why are symbols in my binaries ?

## Code
gcc main.c -g -o main
llvm-readelf --sections main
batcat main.c
nm main
nm -D main

## Text
> Welcome everybody, today we will talk about the meta-information added to your binaries during the build process — the so-called symbols.
> In the following, I differentiate between three types of symbols:
Debug symbols, symbols for static linking, and symbols for dynamic linking.
Btw. what we see here are their related sections within the binary.

The Debug symbols provide extra information used when debugging.
They are added by default in Rust, and in Clang or GCC when compiling with the -g flag.

To easier understand the symbols for linking, let's switch to the following code snippet.
During compilation, the compiler creates a symbol for everything that will receive a permanent memory address later on.
This way, the linker has a reference to work with.

You can inspect the symbols of the resulting binary using nm.
Here we can see that there is indeed a symbol for everything except local variables.
Local variables live on the stack, which means they have no permanent memory address, which means the linker does not care about them, and therefore they do not need a symbol.

The difference between static and dynamic symbols is the following:

Static symbols are resolved during build time.
The code from libraries is copied into the final executable.

Dynamic Symbols on the other hand are resolved during runtime by dynamically linking shared libraries — for example, the standard C library.

> So the big question is: "Why do we need static symbols after build time?"
> And the answer is — we don't.

> In fact, there are several reasons why we should strip them, at least in our release builds.
> But that’s the topic of the next episode.

> So I hope to see you soon, and thank you for watching!


