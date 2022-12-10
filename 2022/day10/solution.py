"""
Day 10: Cathode-Ray Tube

Part 1: 
Part 2: 
"""

def parse_data(f):
    return [a.split() for a in f.read().splitlines()]

def part1(data):
    cycle = 0
    x = 1
    total = 0
    for instr in data:
        cycle += 1

        if cycle in [20, 60, 100, 140, 180, 220]:
            total += cycle * x

        if instr[0] == 'addx':
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                total += cycle * x

            x += int(instr[1])


    return total


def part2(data):
    cycle = 0
    x = 1

    screen = [[' ' for _ in range(40)] for _ in range(6)]
    for instr in data:
        row, col = cycle // 40, cycle % 40
        if col in range(x-1, x+2):
            screen[row][col] = '█'

        cycle += 1

        if instr[0] == 'addx':
            row, col = cycle // 40, cycle % 40
            if col in range(x-1, x+2):
                screen[row][col] = '█'

            cycle += 1

            x += int(instr[1])
            x %= 40

    return '\n' + '\n'.join([''.join(a) for a in screen])
