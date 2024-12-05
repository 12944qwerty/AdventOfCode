"""
Day 13: Mine Cart Madness

Part 1: 
Part 2: 
"""
import re
from functools import lru_cache
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from math import gcd, lcm, floor, ceil, sqrt, prod
from utils import *

def parse_data(f):
    return [a for a in f.read().split("\n")]

def part1(data):
    g = Grid.from_list(data)
    carts = []
    for coord, c in g.items():
        if c in "<>^v":
            carts.append([coord, "|" if c in "^v" else "-", 0])
    
    tick = 0
    while True:
        for i, (cart, rail, turns) in enumerate(carts):
            cx, cy = cart
            dir = g[cart]
            if g[cart] == "^":
                cy -= 1
            elif g[cart] == "v":
                cy += 1
            elif g[cart] == "<":
                cx -= 1
            elif g[cart] == ">":
                cx += 1
            g[cart] = rail
            cart = (cx, cy)
            carts[i] = [cart, g[cart], turns]
            if g[cart] in "<>^v":
                return ",".join(map(str, cart))
            if g[cart] == "/":
                if dir == "^":
                    g[cart] = ">"
                elif dir == "v":
                    g[cart] = "<"
                elif dir == "<":
                    g[cart] = "v"
                elif dir == ">":
                    g[cart] = "^"
            elif g[cart] == "\\":
                if dir == "^":
                    g[cart] = "<"
                elif dir == "v":
                    g[cart] = ">"
                elif dir == "<":
                    g[cart] = "^"
                elif dir == ">":
                    g[cart] = "v"
            elif g[cart] == "+":
                if turns % 3 == 0:
                    g[cart] = "<^>v"["<^>v".index(dir) - 1]
                if turns % 3 == 1:
                    g[cart] = dir
                if turns % 3 == 2:
                    g[cart] = "v>^<"["v>^<".index(dir) - 1]
                carts[i][2] += 1
            else:
                g[cart] = dir

def part2(data):
    g = Grid.from_list(data)
    carts = []
    for coord, c in g.items():
        if c in "<>^v":
            carts.append([coord, "|" if c in "^v" else "-", 0, False, c])
    
    tick = 0
    prev = ""
    while sum(not dead for _, _, _, dead, _ in carts) > 1:
        tick += 1
        carts = sorted(carts, key=lambda a: (a[0][1], a[0][0]))
        for i, (cart, rail, turns, dead, dir) in enumerate(carts):
            if dead: continue
            cx, cy = cart
            if dir == "^":
                cy -= 1
            elif dir == "v":
                cy += 1
            elif dir == "<":
                cx -= 1
            elif dir == ">":
                cx += 1
            g[cart] = rail
            cart = (cx, cy)
            carts[i] = [cart, g[cart], turns, dead, dir]
            if g[cart] in "<>^v":
                for j, (cart2, _, _, d,di) in enumerate(carts):
                    if cart2 == cart and not d and i != j:
                        carts[i][3] = True
                        carts[j][3] = True
                        g[cart] = carts[j][1]
                        break
                continue
            if g[cart] == "/":
                if dir == "^":
                    g[cart] = ">"
                elif dir == "v":
                    g[cart] = "<"
                elif dir == "<":
                    g[cart] = "v"
                elif dir == ">":
                    g[cart] = "^"
            elif g[cart] == "\\":
                if dir == "^":
                    g[cart] = "<"
                elif dir == "v":
                    g[cart] = ">"
                elif dir == "<":
                    g[cart] = "^"
                elif dir == ">":
                    g[cart] = "v"
            elif g[cart] == "+":
                if turns % 3 == 0:
                    g[cart] = "<^>v"["<^>v".index(dir) - 1]
                if turns % 3 == 1:
                    g[cart] = dir
                if turns % 3 == 2:
                    g[cart] = "v>^<"["v>^<".index(dir) - 1]
                carts[i][2] += 1
            else:
                g[cart] = dir
            carts[i][4] = g[cart]

    for i, (_, _, _, dead, _) in enumerate(carts):
        if not dead:
            return ",".join(map(str, carts[i][0]))
