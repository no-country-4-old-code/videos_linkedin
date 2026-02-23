# 014_hack_DOOM_1 - PreLoad Technique

## Concept
Demonstrate LD_PRELOAD to inject custom code into existing programs without modifying them.

## Key Points
- LD_PRELOAD hijacks dynamic library loading
- Replace any library function with custom implementation
- Use case: hooking, debugging, testing, security research
- Demonstrate by modifying DOOM or another game behavior
- Show how to intercept specific functions
- Security implications: privilege escalation if misconfigured

## Hook
"How to hack any program without touching a single byte of its code. Welcome to LD_PRELOAD."

## Practical Demo
- Create shared library intercepting `rand()` function
- Use LD_PRELOAD to make game predictable
- Show original vs modified behavior
- Intercept `write()` syscall to log output
- Demonstrate with real program (DOOM, game, or CLI tool)
- Show how to detect preloaded libraries
- Mention security: why SUID programs ignore LD_PRELOAD
