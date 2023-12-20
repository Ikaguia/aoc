import sys

total = 0

real = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

for i, line in enumerate(sys.stdin):
    line = line.rstrip()
    game = {}
    draws = line.split(":")[1]
    for draw in draws.split(";"):
        for cube in draw.split(','):
            quant, color = cube.split()
            game[color] = max(game.get(color, 0), int(quant))
    for color in game.keys():
        if game.get(color, 0) > real[color]:
            break
    else:
        total += i+1
print(total)