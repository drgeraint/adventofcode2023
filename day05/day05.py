#! /usr/bin/env python3

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

idxs = {}
maps = {}
seeds = set()

seeds_str = lines[0].split('seeds: ')[1].split()
for seed in seeds_str: seeds.add(int(seed))

for line in lines[1:-1]:
    if '' == line:
        pass
    else:
        parts = line.split()
        if "map:" == parts[1]:
            name = parts[0]
            maps[name] = {}
            idxs[name] = []
        else:
            dst = int(parts[0])
            src = int(parts[1])
            num = int(parts[2])
            maps[name][(src)] = {'span': num, 'diff': dst-src}
            idxs[name].append(src)

for k, v in idxs.items():
    idxs[k].sort()

def lookup(map_name, val):
    idx = idxs[map_name].copy()
    if val in idx:
        rec = maps[map_name][(val)]
        dif = rec['diff']
        dst = val + dif
    else:
        idx.append(val)
        idx.sort()
        i = idx.index(val)
        if 0 == i:
            dst = val
        else:
            src = idx[i-1]
            rec = maps[map_name][(src)]
            spn = rec['span']
            if val in range(src, src+spn):
                dif = rec['diff']
                dst = val + dif
            else:
                dst = val
    #print(map_name, val, dst)
    return dst
                    
min_location = 9999999999999999999
for seed in seeds:
    soil        = lookup('seed-to-soil',            seed)
    fertilizer  = lookup('soil-to-fertilizer',      soil)
    water       = lookup('fertilizer-to-water',     fertilizer)
    light       = lookup('water-to-light',          water)
    temperature = lookup('light-to-temperature',    light)
    humidity    = lookup('temperature-to-humidity', temperature)
    location    = lookup('humidity-to-location',    humidity)
    #print(seed, soil, fertilizer, water, light, temperature, humidity, location)
    if int(location) < min_location:
        min_location = int(location)
        min_seed     = seed

print('Answer 1:', min_location)

