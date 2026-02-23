# 027_CPU_vulnerabilities - System CPU Vulnerability Status

## Concept
Show how to check CPU vulnerabilities on Linux systems and what they mean.

## Key Points
- `/sys/devices/system/cpu/vulnerabilities/` contains all CPU vulns
- Common vulnerabilities: Meltdown, Spectre, MDS, L1TF, Zombieload
- Each file shows status: Vulnerable, Mitigation, Not affected
- Mitigations have performance impact
- Show how to check current kernel mitigations
- Explain basic principle of each major vulnerability

## Hook
"Your CPU has vulnerabilities you can't patch. But you can check them."

## Practical Demo
- `ls /sys/devices/system/cpu/vulnerabilities/`
- `cat` each vulnerability file to show status
- Explain what each vulnerability means (one-liner each)
- Show enabled mitigations in `/proc/cmdline`
- Check `lscpu` for vulnerability summary
- Demonstrate performance impact with mitigations on/off (if possible)
- Show how to disable mitigations (not recommended) for testing
- Check CPU flags with `grep flags /proc/cpuinfo`
