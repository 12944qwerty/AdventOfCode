"""
Day 10: Syntax Scoring

Part 1: 
Part 2: 
"""

close = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def parse_data(f):
    return f.read().splitlines()

def part1(data):
    total = 0

    for line in data:
        prev = ""
        while prev != line:
            prev = line
            line = line.replace("()", "").replace("[]", "").replace("{}", "").replace("<>", "")

        for i in line:
            if i in close:
                total += close[i]
                break

    return total

def part2(data):
    total = 0

    o = " ([{<"
    total = []
    for line in data:
        prev = ""
        while prev != line:
            prev = line
            line = line.replace("()", "").replace("[]", "").replace("{}", "").replace("<>", "")

        for i in close:
            if i in line:
                break
        else:
            t = 0
            for i in line[::-1]:
                t = t * 5 + o.index(i)
            total.append(t)
            
    return sorted(total)[len(total) // 2]
