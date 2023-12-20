import sys, re

schematic = [ line.rstrip() for line in sys.stdin ]
numbers = [[] for _ in range(len(schematic))]
gears = []

for i, line in enumerate(schematic):
    for match in re.finditer(r'\d+', line):
        numbers[i].append({
            'val': int(match.group(0)),
            'span': match.span(),
        })
    for match in re.finditer(r'\*', line):
        gears.append({
            'x': match.start(),
            'y': i,
        })

total = 0

# print(numbers)
# print(gears)
# print(schematic)

for g in gears:
    _numbers = []
    # print(numbers)
    # print(max(0, g["y"] -1), min(len(schematic), g["y"]+2))
    # print(numbers[max(0, g["y"] -1):min(len(schematic), g["y"]+2)])
    for ns in numbers[max(0, g["y"] -1):min(len(schematic), g["y"]+2)]:
        for n in ns:
            if not (n["span"][0]-1) <= g["x"] <= (n["span"][1]): continue
            _numbers.append(n["val"])
    if len(_numbers) == 2:
        total += _numbers[0] * _numbers[1]
    # print(g, _numbers)

print(total)
