"""
Day 03: Gear Ratios

Part 1: 
Part 2: 
"""

def parse_data(f):
    return [list(a) for a in f.read().splitlines()]

def part1(data):
    parts = {}
    for i in range(len(data)):
        numstart = (0, 0)
        innum = False
        for j in range(len(data[i])):
            if data[i][j] in '0123456789':
                if innum:
                    parts[numstart][1] = (i, j)
                    parts[numstart][0] += data[i][j]
                else:
                    numstart = (i, j)
                    parts[numstart] = [data[i][j], (i, j)]
                    innum = True
            else:
                innum = False
                
    sum = 0
                
    for start, (num, end) in parts.items():
        for x in range(start[1], end[1]+1):
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                nx, ny = x + dx, start[0] + dy
                if nx < 0 or nx >= len(data[0]) or ny < 0 or ny >= len(data):
                    continue
                if data[ny][nx].lower() in '0123456789abcdefghijklmnopqrstuvwxyz.':
                    continue
                
                break
            else:
                continue
            break
        else:
            continue
        
        sum += int(num)

    return sum
            

def part2(data):
    parts = {}
    gears = {}
    for i in range(len(data)):
        numstart = (0, 0)
        innum = False
        for j in range(len(data[i])):
            if data[i][j] in '0123456789':
                if innum:
                    parts[numstart][1] = (i, j)
                    parts[numstart][0] += data[i][j]
                else:
                    numstart = (i, j)
                    parts[numstart] = [data[i][j], (i, j)]
                    innum = True
            elif data[i][j] == "*":
                gears[(i, j)] = set()
                innum = False
            else:
                innum = False   
                
    for start, (num, end) in parts.items():
        for x in range(start[1], end[1]+1):
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                nx, ny = x + dx, start[0] + dy
                if nx < 0 or nx >= len(data[0]) or ny < 0 or ny >= len(data):
                    continue
                if data[ny][nx].lower() in '0123456789abcdefghijklmnopqrstuvwxyz.':
                    continue
                
                if data[ny][nx] == "*":
                    gears[(ny, nx)].add(num)
                
                break
            else:
                continue
            break
        else:
            continue
        
    sum = 0
        
    for _, parts in gears.items():
        if len(parts) == 2:
            sum += int(list(parts)[0]) * int(list(parts)[1])
            
    return sum
