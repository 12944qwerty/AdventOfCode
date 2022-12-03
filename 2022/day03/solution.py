"""
Day 03: Rucksack Reorganization

Part 1: Sum up the "letters" that are common between the halves on each line
Part 2: Sum up the "letters" that are common between groups of 3 lines
"""

with open('data.txt', encoding='utf-8') as f:
    data = f.readlines()

ABC = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
for i in data:
    mid = len(i)//2
    a, b = i[:mid], i[mid:]

    for j in set(a):
        if j in b:
            total += ABC.index(j)

print("Part 1:", total)

total = 0
for i in range(len(data)//3):
    a = data[i*3].strip()
    b = data[i*3+1].strip()
    c = data[i*3+2].strip()

    for j in set(a):
        if j in b and j in c:
            total += ABC.index(j)

print("Part 2:", total)
