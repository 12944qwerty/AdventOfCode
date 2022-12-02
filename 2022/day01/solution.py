"""
Day 01: Calorie Counting

Part 1: Get the amount of calories the elf who is carrying the most has.
Part 2: Get the top 3 elves who hold the most calories, and sum them.
"""

with open('data.txt', encoding='utf-8') as f:
    data = [sum(list(map(int,a.split('\n')))) for a in f.read().split('\n\n')]

data.sort(reverse=True)

print("Part 1:", data[0])
print("Part 2:", sum(data[:3]))
