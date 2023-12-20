import sys, re

total = 0

for line in sys.stdin:
    line = line.rstrip()
    for i,number in enumerate(("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")):
        line = line.replace(number, number + str(i+1) + number)
    digits = ''.join(d for d in line if d.isdigit())
    total += 10*int(digits[0]) + int(digits[-1])
    print(10*int(digits[0]) + int(digits[-1]))

print(total)
