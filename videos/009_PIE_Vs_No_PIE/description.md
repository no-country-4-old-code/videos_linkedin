# 009_PIE_Vs_No_PIE - Position Independent Executables

## Concept
Explain the difference between PIE and No-PIE binaries and their security implications.

## Key Points
- No-PIE: executable code at fixed memory addresses (predictable)
- PIE: executable code can be loaded at random addresses (works with ASLR)
- Show compilation flags: `-fPIE -pie` vs `-no-pie`
- Use `readelf -h` to check if binary is PIE or not
- Demonstrate address differences when running PIE binaries multiple times
- Explain performance trade-off (minimal) vs security benefit (significant)

## Hook
"Two identical programs, but one is 10x harder to exploit. The difference? Just three letters: PIE."

## Practical Demo
- Compile with and without PIE
- Check binary type with `file` and `readelf`
- Print function addresses in both versions
- Show that No-PIE always loads at 0x400000
- Show that PIE loads at random addresses
- Demonstrate attempted ROP attack failing with PIE
