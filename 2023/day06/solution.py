"""
Day 06: Wait For It

Part 1: 
Part 2: 
"""
import re

def parse_data(f):
    return f.read().splitlines()

def part1(data):
    reg = re.compile(r'\d+')
    
    times = list(map(int, reg.findall(data[0])))
    records = list(map(int, reg.findall(data[1])))
    
    prod = 1
    for i, time in enumerate(times):
        wr = records[i]
        
        h = 0
        for i in range(time):
            if (time - i) * i > wr:
                h += 1
        
        prod *= h
        
    return prod
        

def part2(data):
    reg = re.compile(r'\d+')
    data = [line.replace(" ", "") for line in data]
    
    time = list(map(int, reg.findall(data[0])))[0]
    record = list(map(int, reg.findall(data[1])))[0]
    
    h = 0
    for i in range(time):
        if (time - i) * i > record:
            h += 1
            
    return h
