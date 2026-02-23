# 016_Hack_ShellCodeInjection - Why NX Protection Exists

## Concept
Demonstrate shellcode injection attack and show why NX (No-Execute) bit is crucial for security.

## Key Points
- Buffer overflow to inject malicious code
- Execute injected code on the stack
- Show attack without NX protection (executable stack)
- Show attack failure with NX protection
- Compile flags: `-z execstack` vs `-z noexecstack`
- Check NX status with `readelf -l` and look for GNU_STACK

## Hook
"Write 64 bytes into a 32-byte buffer, and suddenly you're running your own code. Unless NX stops you."

## Practical Demo
- Vulnerable C program with buffer overflow
- Craft exploit with shellcode (spawn shell)
- Demonstrate successful exploit without NX
- Recompile with NX protection
- Show exploit failure (segmentation fault)
- Use `execstack -q` to check executable stack
- Brief mention of ROP as NX bypass technique
