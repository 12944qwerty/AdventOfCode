"""
Day 04: Scratchcards

Part 1: 
Part 2: 
"""
import re

def parse_data(f):
    return f.read().splitlines()

def part1(data):
    reg = re.compile(r"\d+")
    sum = 0
    for line in data:
        score = 0
        line = line.split(": ")[1].strip().split(" | ")
        mine = reg.findall(line[1])
        for winning in reg.findall(line[0]):
            if winning in mine:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        
        sum += score
        
    return sum

def part2(data):
    reg = re.compile(r"\d+")    
    cards = {}
    
    for line in data:
        line = line.split(": ")
        
        num = reg.findall(line[0])[0]
        nums = line[1].strip().split(" | ")
        winnings = reg.findall(nums[0])
        mine = reg.findall(nums[1])
        
        next = 0
        for win in winnings:
            if win in mine:
                next += 1
        
        cards[num] = [next, 0]
    
    for card in cards:
        cards[card][1] += 1
        for j in range(cards[card][0]):
            cards[str(int(card)+1+j)][1] += 1 * cards[card][1]
    
    return sum(a[1] for a in cards.values())
