"""
Day 07: No Space Left On Device

Part 1: Find the sum of the sizes of directories that are less than 100000
Part 2: Find the smallest size directory that will empty the disk to at least 30000000
"""

def parse_data(f):
    data = f.read().splitlines()


    tree = {'/': {}}
    current = []
    possibleDirs = set()
    inDir = False
    for line in data:
        if line.startswith('$'):
            inDir = False
            cmd = line.split()
            if cmd[1] == 'cd':
                if cmd[2] == '..':
                    current = current[:-1]
                else:
                    current.append(cmd[2])
                possibleDirs.add('uniquesplitter'.join(current))

                exec("if len(current) > 1 and '" + current[-1] + "' not in tree['" + "']['".join(current[:-1]) + "']: tree['" + "']['".join(current) + "'] = {}")
            elif cmd[1] == 'ls':
                inDir = True
            continue
        if inDir: # should be true if not prefixed
            file_ = line.split()
            if file_[0] != 'dir':
                exec("tree['" + "']['".join(current) + f"']['{file_[1]}'] = {file_[0]}")
    
    return tree, possibleDirs

def add_total(stuff):   
    total = 0
    for value in stuff.values():
        if isinstance(value, int):
            total += value
        else:
            total += add_total(value)
    return total

def part1(data):
    tree, possibleDirs = data
    
    bigtotal = 0

    for dirs in possibleDirs:
        current = dirs.split('uniquesplitter')

        stuff = tree
        for dir in current:
            stuff = stuff.get(dir)

        total = add_total(stuff)

        if total < 100000:
            bigtotal += total

    return bigtotal


def part2(data):
    tree, possibleDirs = data

    free = 30000000 - (70000000 - add_total(tree['/']))

    couldDelete = []

    for dirs in possibleDirs:
        current = dirs.split('uniquesplitter')

        stuff = tree
        for dir in current:
            stuff = stuff.get(dir)

        total = add_total(stuff)

        if total > free:
            couldDelete.append(total)

    return min(couldDelete)
