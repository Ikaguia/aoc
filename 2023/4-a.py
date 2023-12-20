import sys

total = 0

for line in sys.stdin:
    card = line.strip().split(':')[1]
    win_n, elf_n = card.split('|')
    win_n = {int(n) for n in win_n.strip().split()}
    elf_n = {int(n) for n in elf_n.strip().split()}
    common_n = win_n.intersection(elf_n)
    if len(common_n):
        total += 2**(len(common_n)-1)

print(total)