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
    seeds = list(map(int, data[0][0].split(": ")[1].split(" ")))   
    
    mapping = {}
    for cat in data[1:]:
        key = cat[0].split(" map:")[0]
        mapping[key] = []
        for line in cat[1:]:
            vals = list(map(int, line.split(" ")))
            mapping[key].append(vals)
            
    newseeds = []
    
    i = 0
    for a in range(0, len(seeds), 2):
        for seed in range(seeds[a], seeds[a] + seeds[a+1]+1):
            for key, val in mapping.items():
                for entry in val:
                    if seed >= entry[1] and seed < entry[1] + entry[2]:
                        seed = seed - entry[1] + entry[0]
                        break
            newseeds.append(seed)   
            i += 1
            if i % 1000000 == 0:
                print(i) 
    return min(newseeds)
