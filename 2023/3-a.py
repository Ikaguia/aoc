import sys, re

numbers = []

schematic = []

for i, line in enumerate(sys.stdin):
    line = line.rstrip()
    for match in re.finditer(r'\d+', line):
        numbers.append({
            'val': int(match.group(0)),
            'span': match.span(),
            'height': i,
        })
    schematic.append(line)

total = 0

# print(numbers)
# print(schematic)

for n in numbers:
    added = False
    # print(n["val"])
    # print(n["height"], max(0, n["height"] -1), min(len(schematic), n["height"]+2))
    # print(n["span"], max(0, n["span"][0]-1), min(len(schematic[0]), n["span"][1]+1))
    for y in range(max(0, n["height"] -1), min(len(schematic), n["height"]+2)):
        if added: continue
        for x in range(max(0, n["span"][0]-1), min(len(schematic[y]), n["span"][1]+1)):
            if not added and schematic[y][x] != '.' and not schematic[y][x].isdigit():
                added = True
                total += n["val"]
    # print(n["val"], added)

print(total)
