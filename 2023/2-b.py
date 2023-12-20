import sys, functools

total = 0

for i, line in enumerate(sys.stdin):
    line = line.rstrip()
    game = {}
    draws = line.split(":")[1]
    for draw in draws.split(";"):
        for cube in draw.split(','):
            quant, color = cube.split()
            game[color] = max(game.get(color, 0), int(quant))

    power = functools.reduce(lambda a,b: a*b, game.values(), 1)
    # print(power, game)
    total += power
print(total)