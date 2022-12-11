"""
Day 11: Monkey in the Middle

Part 1: 
Part 2: 
"""

import re

reg = re.compile("Monkey (\d):\n +?Starting items:((?: \d+,?)+)\n +?Operation: new = old (.+?)\n +? Test: divisible by (\d+?)\n +?If true: throw to monkey (\d+?)\n +? If false: throw to monkey (\d+?)")

def parse_data(f):
    data = [reg.match(a.strip()).groups() for a in f.read().split('\n\n')]
    monkeys = {}

    for monkey in data:
        monkeys[monkey[0]] = {
            "items": list(map(int, monkey[1].split(', '))),
            "op": monkey[2],
            "test": int(monkey[3]),
            "throw": [monkey[5], monkey[4]],
            "inspections": 0
        }

    return monkeys

def part1(monkeys):
    for _ in range(20):
        for num in monkeys:
            data = monkeys[num]
            for _ in "0" * len(data["items"]):
                item = data['items'][0]
                item = eval(f'{item} {data["op"].replace("old", str(item))}') // 3
                monkeys[data['throw'][item % data['test'] == 0]]['items'].append(item)
                data['items'] = data['items'][1:]
                data['inspections'] += 1
    
    m = sorted(list(monkeys.values()), key=lambda a: a["inspections"])
    return m[-1]["inspections"] * m[-2]["inspections"]

def part2(monkeys):
    DIVS = [monkeys[a]["test"] for a in monkeys]
    prod = 1
    for i in DIVS:
        prod *= i

    for i in range(10000):
        for num in monkeys:
            data = monkeys[num]
            for _ in "0" * len(data["items"]):
                item = data['items'][0] % prod
                item = eval(f'{item} {data["op"].replace("old", str(item))}')
                monkeys[data['throw'][item % data['test'] == 0]]['items'].append(item)
                data['items'] = data['items'][1:]
                data['inspections'] += 1
    
    m = sorted(list(monkeys.values()), key=lambda a: a["inspections"])
    return m[-1]["inspections"] * m[-2]["inspections"]
