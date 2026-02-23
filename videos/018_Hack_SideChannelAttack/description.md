# 018_Hack_SideChannelAttack - Meltdown Demonstration

## Concept
Explain side-channel attacks focusing on CPU vulnerabilities like Meltdown that leak data through timing.

## Key Points
- Side-channels exploit timing, power, EM radiation, etc.
- Meltdown exploits speculative execution to read kernel memory
- Demonstrate timing difference between cached and uncached memory
- Show proof-of-concept reading protected memory
- Explain why software can't fully fix hardware vulnerabilities
- Check system vulnerability: `/sys/devices/system/cpu/vulnerabilities/`

## Hook
"Your CPU is so fast, it accidentally leaks secrets. Welcome to side-channel attacks."

## Practical Demo
- Check CPU vulnerabilities in `/sys/devices/system/cpu/vulnerabilities/`
- Simple timing attack to detect cached data
- Demonstrate cache-timing attack principles
- Show Meltdown PoC reading kernel memory (if available)
- Use `perf` to measure cache hits/misses
- Discuss mitigations (KPTI) and performance impact
- Show why this affects all modern CPUs
