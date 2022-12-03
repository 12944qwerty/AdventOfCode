"""
Day 02: Rock Paper Scissors

A,X = Rock - B,Y = Paper - C,Z = Scissors
   1 point      2 points         3 points

Draw = 3 points, Win = 6 points

Part 1: Get the total amount of points based on the choices given

X = Lose, Y = Draw, Z = Win
Part 2: Get the total amount of points based on the win/lose choices given
"""

def parse_data(f):
    return [a.split() for a in f.readlines()]

def part1(data):
    total = 0

    for a,b in data:
        total += "XYZ".index(b) + 1
        total += "AX BY CZ AY BZ CX AY BZ CX".count(a+b) * 3

    return total

def part2(data):
    total = 0

    for a,b in data:
        if b == 'X': # lose
            total += "BCA".index(a) + 1
        elif b == 'Y': # tie
            total += 4 + "ABC".index(a)
        else: # win
            total += 7 + "CAB".index(a)
    
    return total
