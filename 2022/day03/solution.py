"""
Day 03: Rucksack Reorganization

Part 1: Sum up the "letters" that are common between the halves on each line
Part 2: Sum up the "letters" that are common between groups of 3 lines
"""

with open('data.txt', encoding='utf-8') as f:
    data = f.read().splitlines()

ABC = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
for i in data:
    mid = len(i)//2
    a, b = i[:mid], i[mid:]

    for j in set(a) & set(b):
        total += ABC.index(j)

print("Part 1:", total)

total = 0
for i in range(0, len(data), 3):
    a, b, c = map(set, data[i:i+3])

    for j in a & b & c:
        total += ABC.index(j)

print("Part 2:", total)
