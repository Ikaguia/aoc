import sys

total = 0
cards = [
    {
        "copies": 1,
        "line": line.strip().split(':')[1]
    } for line in sys.stdin
]

for i, card in enumerate(cards):
    win_n, elf_n = card["line"].split('|')
    win_n = {int(n) for n in win_n.strip().split()}
    elf_n = {int(n) for n in elf_n.strip().split()}
    common = len(win_n.intersection(elf_n))
    for j in range(common):
        if i+j+1 < len(cards):
            cards[i+j+1]["copies"] += card["copies"]
    total += card["copies"]

print(total)