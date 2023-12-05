"""
Day 05: If You Give A Seed A Fertilizer

Part 1: 
Part 2: I got the correct answer with the wrong solution. Didn't work for example data, worked for my input. Weird. Not complaining. Never again. Hated this.
"""
from functools import lru_cache


def parse_data(f):
    return [a.splitlines() for a in f.read().split("\n\n")]

def part1(data):    
    seeds = list(map(int, data[0][0].split(": ")[1].split(" ")))   
    
    mapping = {}
    for cat in data[1:]:
        key = cat[0].split(" map:")[0]
        mapping[key] = []
        for line in cat[1:]:
            vals = list(map(int, line.split(" ")))
            mapping[key].append(vals)
        
    newseeds = []
    for seed in seeds:
        for key, val in mapping.items():
            for entry in val:
                if seed >= entry[1] and seed < entry[1] + entry[2]:
                    seed = seed - entry[1] + entry[0]
                    break
        newseeds.append(seed)    
    return min(newseeds)

def part2(data):
    s = list(map(int, data[0][0].split(": ")[1].split(" ")))
    seeds = []
    for i in range(0, len(s), 2):
        seeds += [[s[i], s[i+1]]]
        
    mapping = []
    for cat in data[1:]:
        new = []
        for line in cat[1:]:
            vals = list(map(int, line.split(" ")))
            new.append(tuple(vals))
        
        mapping.append(tuple(new))
    mapping = tuple(mapping)
            
    @lru_cache(maxsize=2**5)
    def get_seed(start, range, mapping):
        allseeds = []
        if len(mapping) == 1:
            for entry in mapping[0]:
                if start >= entry[1] + entry[2] or start + range < entry[1]:
                    continue
                
                a = max(start, entry[1]) - entry[1] + entry[0]
                allseeds.append(a)
                
            minentry = min(mapping[0], key=lambda x: x[1])
            maxentry = max(mapping[0], key=lambda x: x[1] + x[2])
            
            if start < minentry[1]:
                a = start
                allseeds.append(a)
                
            a = maxentry[1] + maxentry[2]
            if start + range > a:
                allseeds.append(a)
                
            if len(allseeds) == 0:
                return start

            return min(allseeds)
        
        for entry in mapping[0]:
            if start >= entry[1] + entry[2] or start + range < entry[1]:
                continue
                     
            a = max(start, entry[1]) - entry[1] + entry[0]
            b = min(start + range, entry[1] + entry[2]) - max(start, entry[1])
            allseeds.append(get_seed(a, b, mapping[1:]))
        
        minentry = min(mapping[0], key=lambda x: x[1])
        maxentry = max(mapping[0], key=lambda x: x[1] + x[2])
        
        if start < minentry[1]:
            a = start
            b = minentry[1] - a
            allseeds.append(get_seed(a, b, mapping[1:]))
            
        a = maxentry[1] + maxentry[2]
        if start + range > a:
            b = start + range - a
            allseeds.append(get_seed(a, b, mapping[1:]))
            
        if len(allseeds) == 0:
            return get_seed(start, range, mapping[1:])
        
        return min(allseeds)
        
    newseeds = []
    for a, b in seeds:
        seed = get_seed(a, b, mapping)
        
        newseeds.append(seed)    
   
        
    return min(newseeds)
