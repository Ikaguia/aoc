import sys, re

total = 0

for line in sys.stdin:
    line = line.rstrip()
    digits = ''.join(d for d in line if d.isdigit())
    total += 10*int(digits[0]) + int(digits[-1])

print(total)
