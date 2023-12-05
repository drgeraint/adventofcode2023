#! /usr/bin/env python3

#with open('test1.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

idxs = {}
maps = {}
seeds = set()

seed_list = lines[0].split('seeds: ')[1].split()
for seed in seed_list: seeds.add(int(seed))

for line in lines[1:-1]:
    if '' == line:
        pass
    else:
        parts = line.split()
        if "map:" == parts[1]:
            name = parts[0]
            x,y,z = name.split('-')
            name_fwd = name
            name_rev = z+'-'+y+'-'+x
            maps[name_fwd] = {}
            maps[name_rev] = {}
            idxs[name_fwd] = []
            idxs[name_rev] = []
        else:
            dst = int(parts[0])
            src = int(parts[1])
            num = int(parts[2])
            maps[name_fwd][(src)] = {'span': num, 'diff': dst-src}
            maps[name_rev][(dst)] = {'span': num, 'diff': src-dst}
            idxs[name_fwd].append(src)
            idxs[name_rev].append(dst)

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

locations  = []
for k, v in maps['location-to-humidity'].items():
    if k <= min_location:
        locations.append(k)

target_seeds = []
seed_location = {}
for location in locations:
    humidity	= lookup('location-to-humidity',	location)
    temperature	= lookup('humidity-to-temperature',	humidity)
    light	= lookup('temperature-to-humidity',	temperature)
    water	= lookup('light-to-water',		light)
    fertilizer	= lookup('water-to-fertilizer',		water)
    soil	= lookup('fertilizer-to-soil',		fertilizer)
    seed	= lookup('soil-to-seed',		soil)
    target_seeds.append(seed)
    seed_location[seed] = location
    print('location:', location, 'seed:', seed)
    
print('target_seeds:', target_seeds)

maps['seeds2'] = {}
idxs['seeds2'] = []
for i in range(0, len(seed_list), 2):
    src = int(seed_list[i])
    num = int(seed_list[i+1])
    maps['seeds2'][(src)] = {'span': num}
    idxs['seeds2'].append(src)
    
def lookup2(map_name, val):
    idx = idxs[map_name].copy()
    if val in idx:
        retval = val        
    else:
        idx.append(val)
        idx.sort()
        i = idx.index(val)
        if 0 == i:
            retval = None
        else:
            src = idx[i-1]
            rec = maps[map_name][(src)]
            spn = rec['span']
            if val in range(src, src+spn):
                retval = val
            else:
                retval = None
    return retval

best_seed = None
i = 0
while best_seed is None:
    best_seed = lookup2('seeds2', target_seeds[i])
    i = i+1
print('best_seed:', best_seed, 'location:', seed_location[best_seed])
print('Answer 2:', seed_location[best_seed])

