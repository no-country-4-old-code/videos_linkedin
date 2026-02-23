# 019_HackMe_SimpleHackMe - Simple Binary Exploitation Challenge

## Concept
Create and solve a beginner-friendly binary exploitation challenge (buffer overflow).

## Key Points
- Simple vulnerable program that checks a password
- Buffer overflow vulnerability to bypass authentication
- Use `gdb` to analyze and find the overflow
- Calculate exact offset with pattern_create/pattern_offset
- Overwrite return address or local variable
- No modern protections (no NX, no ASLR, no PIE, no stack canary)

## Hook
"This program wants a password. But I have something better: 100 A's."

## Practical Demo
- Present vulnerable authentication program
- Show normal behavior with wrong/right password
- Analyze with `gdb` and find vulnerability
- Use pattern to find exact offset
- Craft exploit to bypass authentication
- Show successful privilege escalation
- Explain why this works: memory layout and overwrite
