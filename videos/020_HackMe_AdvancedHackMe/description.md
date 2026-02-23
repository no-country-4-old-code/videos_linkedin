# 020_HackMe_AdvancedHackMe - Intermediate Exploitation Challenge

## Concept
Intermediate-level challenge with some modern protections enabled (NX + ASLR).

## Key Points
- Vulnerable program with NX and ASLR enabled
- Cannot inject shellcode (NX blocks it)
- Need to use ROP or return-to-libc technique
- Information leak to bypass ASLR
- Chain multiple vulnerabilities together
- Use pwntools or manual exploitation

## Hook
"NX and ASLR are enabled. Most attackers would give up. But not us."

## Practical Demo
- Present vulnerable program with modern protections
- Verify protections with `checksec` or `readelf`
- Find and exploit information leak vulnerability
- Leak libc address to defeat ASLR
- Build ROP chain or return-to-libc attack
- Chain exploits together for full compromise
- Show successful shell execution
