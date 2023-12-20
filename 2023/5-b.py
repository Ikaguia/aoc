#need to treat ranges, not gonna bother

import sys, re, bisect

lines = list(line.strip() for line in sys.stdin)

maps = {}
seed_pairs = [int(seed) for seed in lines[0].split(':')[1].strip().split()]
seeds = []
for i, start in enumerate(seed_pairs):
    if i%2: continue
    seeds += [ seed for seed in range(start, start+seed_pairs[i+1]) ]

source = None

for line in lines[2:]:
    if match := re.search(r'(\w+)-to-(\w+) map:', line):
        source, dest = match.groups()
        maps[source] = {
            'dest': dest,
            'map': {}
        }
        print(source, dest)
    elif line:
        dr_start, sr_start, length = map(lambda x: int(x), line.split())
        maps[source]['map'][sr_start] = {
            "sr_start": sr_start,
            "dr_start": dr_start,
            "length": length,
        }

def convert(val, mapping):
    keys = list(mapping.keys())
    keys.sort()
    idx = min(bisect.bisect_right(keys, val)-1, len(keys)-1)
    # print(keys, val, idx)
    if idx == -1: return val
    key = keys[idx]
    # print(key, mapping[key]['length'])
    if mapping[key]['length'] >= (val - key):
        return mapping[key]['dr_start'] + (val - key)
    return val

source = 'seed'
print(seeds, source)
while source != 'location':
    seeds = list(convert(seed, maps[source]['map']) for seed in seeds)
    source = maps[source]['dest']
    print(seeds, source)

seeds.sort()

print(seeds[0])
