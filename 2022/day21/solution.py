"""
Day 21: Monkey Math

Part 1:
Part 2:
"""

HUMN = None

class Node:
    def __init__(self, monkeys, children, parent=None):
        self.parent = parent
        self.name = children
        if children == 'humn':
            global HUMN
            HUMN = self
            return
        children = monkeys[children]
        if len(children) == 1:
            self.value = children[0]
        else:
            self.first = Node(monkeys, children[0], self)
            self.op = children[1]
            self.second = Node(monkeys, children[2], self)

    def __str__(self):
        return f"<Node name={self.name} parent={self.parent}>"


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
