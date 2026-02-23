# 011_syscalls - What's a Syscall

## Concept
Explain system calls as the interface between user programs and the kernel.

## Key Points
- User space vs kernel space
- System calls are the only way to access kernel functions
- Common syscalls: read, write, open, close, fork, execve
- Show syscall numbers in `/usr/include/asm/unistd_64.h`
- Trace syscalls with `strace`
- Show assembly code making syscalls (int 0x80 or syscall instruction)

## Hook
"Every time your program does ANYTHING useful, it's begging the kernel for permission. Let me show you."

## Practical Demo
- Simple program writing "Hello World"
- Trace with `strace ./program`
- Show the write() syscall with arguments
- Minimal assembly program making syscalls directly
- Compare C library call vs raw syscall
- Show syscall overhead with performance measurement
