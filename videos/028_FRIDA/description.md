# 028_FRIDA - Dynamic Instrumentation with Frida

## Concept
Demonstrate how Frida lets you inject JavaScript into running processes to hook functions, inspect memory, and bypass security checks at runtime — no source code needed.

## Key Points
- What Frida is: a dynamic instrumentation toolkit for reverse engineers and pentesters
- Attach to a running process with `frida` CLI
- Hook a function at runtime and intercept its arguments / return value
- Classic demo: hook a password-check function and print the accepted password live
- Works on Linux, macOS, Windows, Android, iOS

## Hook
"This binary checks your password. I'm going to read it back to you — while the program is running."

## Practical Demo
- Compile a small C binary with a hardcoded password check
- Attach Frida to the running process
- Write a small Frida JS script to hook the check function
- Intercept the correct password and print it to the terminal
