with open('data.txt') as f:
    data = [list(map(int,a.split('\n'))) for a in f.read().split('\n\n')]

first = max(data, key=lambda a:sum(a))
data.remove(first)
second = max(data, key=lambda a:sum(a))
data.remove(second)
third = max(data, key=lambda a:sum(a))
data.remove(third)

print("Part 1:", sum(first))
print("Part 2:", sum([*first, *second, *third]))