"""
Day 01: Trebuchet?!

Part 1: 
Part 2: 
"""
import re


def parse_data(f):
    return f.read().splitlines()

def part1(data):
    reg = re.compile(r"\d")
    
    sum = 0    
    for line in data:
        nums = reg.findall(line)
        sum += int(nums[0] + nums[-1])
        
    return sum

def part2(data):
    sum = 0

    mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    
    for line in data:
        nums = []
        for i in range(len(line)):
            if line[i:i+1] in "123456789":
                nums.append(line[i:i+1])
                i += 1
            elif line[i:i+3] in ["one","two","six"]:
                nums.append(mapping[line[i:i+3]])
                i += 3
            elif line[i:i+4] in ["four","five","nine"]:
                nums.append(mapping[line[i:i+4]])
                i += 4
            elif line[i:i+5] in ["three","seven","eight"]:
                nums.append(mapping[line[i:i+5]])
                i += 5
        
        sum += int(nums[0] + nums[-1])
        
    return sum

