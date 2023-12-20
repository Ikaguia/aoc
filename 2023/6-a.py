import sys, math

lines = list(line.strip().replace(' ', '') for line in sys.stdin)
times = list(int(time) for time in lines[0].split(':')[1].split())
distances = list(int(dist) for dist in lines[1].split(':')[1].split())

def calc(time, dist):
    # print(time, dist)

    if math.floor(time/2) * math.ceil(time/2) < dist: return 0
    l, r = 0, math.ceil(time/2)
    # print(f'{l=} {r=}')
    while l != r:
        m = l + math.floor((r-l)/2)
        # print(f'{l=} {r=} {m=}')
        if (m * (time-m)) <= dist: l = m+1
        else: r = m
    L = l

    # print(f'{L=}')

    l,r = math.floor(time/2),time
    # print(f'{l=} {r=}')
    while l != r:
        m = l + math.ceil((r-l)/2)
        # print(f'{l=} {r=} {m=}')
        if (m * (time-m)) <= dist: r = m-1
        else: l = m
    R = r

    # print(f'{R=}')
    print(f'{R-L+1=}')

    return R-L+1

ans = 1
# print(times, distances)
for time, dist in zip(times, distances):
    ans *= calc(time, dist)
print(ans)
