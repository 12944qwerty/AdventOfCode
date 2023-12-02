"""
Day 02: Cube Conundrum

Part 1: 
Part 2: 
"""

def parse_data(f):
    return f.read().splitlines()

def part1(data):
    R = 12
    G = 13
    B = 14
    
    i = 0
    
    for line in data:
        game = int(line.split(": ")[0][5:])
        rounds = line.split(": ")[1].split("; ")
        
        for round in rounds:
            colors = round.split(", ")
            for color in colors:
                if "red" in color:
                    if int(color.split(" ")[0]) > R:
                        break
                elif "green" in color:
                    if int(color.split(" ")[0]) > G:
                        break
                elif "blue" in color:
                    if int(color.split(" ")[0]) > B:
                        break
            else:
                continue
            break
        else:
            i += game
            
    return i
            
def part2(data):
    R = 12
    G = 13
    B = 14
    
    i = 0
    
    for line in data:
        game = int(line.split(": ")[0][5:])
        rounds = line.split(": ")[1].split("; ")
        
        r = 0
        g = 0
        b = 0
        for round in rounds:
            colors = round.split(", ")
            for color in colors:
                if "red" in color:
                    r = max(int(color.split(" ")[0]), r)
                elif "green" in color:
                    g = max(int(color.split(" ")[0]), g)
                elif "blue" in color:
                    b = max(int(color.split(" ")[0]), b)
            else:
                continue
            break
        else:
            i += r * g * b
            
    return i
