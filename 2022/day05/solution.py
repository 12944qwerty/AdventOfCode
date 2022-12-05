"""
Day 05: Supply Stacks

Part 1: Follow the instructions given to move the boxes in each column
Part 2: Follow the instructions given to move the boxes in each column, while maintaining order
"""

import re

def parse_data(f):
    data = f.read()
    boxes_, instr = data.split('\n\n')
    boxes_ = boxes_.splitlines()
    instr = instr.splitlines()
    num = (len(boxes_[-1].replace('  ', ''))-1) // 2
    boxes = [[] for _ in "a"*num]

    for line in boxes_[-2::-1]:
        for i, letter in enumerate(line[1::4]):
            if letter.isalpha():
                boxes[i].append(letter)

    return boxes, instr

def part1(data):
    boxes, instr = data

    reg = re.compile("move (\d{1,2}) from (\d{1,2}) to (\d{1,2})")
    for line in instr:
        count, ind1, ind2 = map(int,reg.match(line).groups())
        for _ in "a"*count:
            boxes[ind2-1].append(boxes[ind1-1].pop())
        
    return "".join(a[-1] for a in boxes)

def part2(data):
    boxes, instr = data

    reg = re.compile("move (\d{1,2}) from (\d{1,2}) to (\d{1,2})")
    for line in instr:
        count, ind1, ind2 = map(int,reg.match(line).groups())
        boxes[ind2-1] += boxes[ind1-1][-count:]
        boxes[ind1-1] = boxes[ind1-1][:-count]
   
    return "".join(a[-1] for a in boxes)
