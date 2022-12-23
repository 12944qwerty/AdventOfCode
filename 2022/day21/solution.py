"""
Day 21: Monkey Math

Part 1: What will the "root" monkey say based on who they're listening for?
Part 2: What do YOU need to say to make the "root" monkey say Truth?
"""

def parse_data(f):
    data = f.read().splitlines()
    for i, item in enumerate(data):
        if len(item) > 10:
            data[i] = [item[:4], item[6:10], item[11:12], item[13:17]]
        else:
            data[i] = item.split(': ')
            data[i][1] = int(data[i][1])

    monkeys = {}
    for monkey in data:
        monkeys[monkey[0]] = monkey[1:]

    return monkeys

def calculate(monkeys, name, humn):
    if name == 'humn' and humn >= 0:
        return humn
    monkey = monkeys[name]

    if len(monkey) == 1:
        return monkey[0]
    else:
        if monkey[1] == '+':
            return calculate(monkeys, monkey[0], humn) + calculate(monkeys, monkey[2], humn)
        if monkey[1] == '-':
            return calculate(monkeys, monkey[0], humn) - calculate(monkeys, monkey[2], humn)
        if monkey[1] == '*':
            return calculate(monkeys, monkey[0], humn) * calculate(monkeys, monkey[2], humn)
        if monkey[1] == '/':
            return calculate(monkeys, monkey[0], humn) / calculate(monkeys, monkey[2], humn)

def part1(data):
    return int(calculate(data, 'root', -1))

def part2(data):
    if calculate(data, data['root'][2], 1) == calculate(data, data['root'][2], 0):
        omg = calculate(data, data['root'][2], -1)
        name = data['root'][0]
    else:
        omg = calculate(data, data['root'][0], -1)
        name = data['root'][2]

    low = 0
    high = int(1e20)
    while low < high:
        mid = (low+high) // 2
        res = calculate(data, name, mid)
        ret = omg - res
        if [ret < 0, ret > 0][globals()['dummy']]:
            low = mid
        elif ret == 0:
            return int(mid)
        else:
            high = mid
