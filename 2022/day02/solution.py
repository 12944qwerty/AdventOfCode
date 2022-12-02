with open('data.txt') as f:
    data = [a.split() for a in f.readlines()]

total = 0
index = " XYZ"

for a,b in data:
    total += index.index(b)
    if a == 'C': # scissors
        if b == 'Z': # scissors
            total += 3
        if b == 'X': # rock
            total += 6
    elif a == 'B': # paper
        if b == 'Y': # paper
            total += 3
        if b == 'Z': # scissors
            total += 6
    else: # rock
        if b == 'X': # rock
            total += 3
        if b == 'Y': # paper
            total += 6

print("Part 1:", total)

total = 0

for a,b in data:
    if b == 'X': # lose
        if a == 'A': # rock
            total += 3 # scissors
        if a == 'B': # paper
            total += 1 # rock
        if a == 'C': # scissors
            total += 2 # paper
    elif b == 'Y': # tie
        total += 3 + " ABC".index(a)
    else: # win
        total += 6
        if a == 'A': # rock
            total += 2 # paper
        if a == 'B': # paper
            total += 3 # scissors
        if a == 'C': # scissors
            total += 1 # rock

print("Part 2:", total)