# 031_Partioning - How Disk Partitioning Actually Works

## Concept
Demystify disk partitioning by showing the on-disk structures (MBR, GPT) that tell the OS where each partition starts and ends — and what can go wrong when they're corrupted or misread.

## Key Points
- MBR vs GPT: structure, limits, and why UEFI needs GPT
- Reading partition tables raw with `fdisk`, `gdisk`, and `hexdump`
- What the partition table bytes actually encode (LBA, size, type GUID)
- Common pitfalls: misaligned partitions, 4K sector vs 512-byte sector mismatch
- How forensics tools recover partitions when the table is wiped

## Hook
"Your disk is just bytes. The partition table is four 16-byte entries — let me show you exactly which ones."

## Practical Demo
- Use `fdisk -l` and `gdisk` to inspect a disk image
- `hexdump` the first 512 bytes of an MBR disk and decode the partition entries by hand
- Compare with a GPT header using `gdisk` expert mode
- Show how `testdisk` can find partitions after the table is zeroed
