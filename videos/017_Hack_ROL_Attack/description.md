# 017_Hack_ROP_Attack - Why ASLR is Critical

## Concept
Demonstrate Return-Oriented Programming (ROP) attack and show why ASLR is essential to defend against it.

## Key Points
- ROP bypasses NX by reusing existing code (gadgets)
- Find gadgets with tools like ROPgadget or ropper
- Chain gadgets to build exploit without injecting code
- Attack works when addresses are predictable (no ASLR)
- Attack fails with ASLR because gadget addresses change
- Combine with format string bugs to leak addresses

## Hook
"NX protects you from injected code. But what if the attacker uses YOUR code against you?"

## Practical Demo
- Vulnerable program with buffer overflow
- Find ROP gadgets with ROPgadget tool
- Build ROP chain to spawn shell
- Exploit works without ASLR (predictable addresses)
- Enable ASLR and show exploit failure
- Demonstrate address randomization across runs
- Mention information leak attacks as ASLR bypass
