"""
Utils Module to quickly work with common concepts.
"""

from .grid import Grid
from .maze import Maze
from .graph import *
import re

number_re = re.compile(r'-?\d+')

def get_numbers(s):
    return list(map(int, number_re.findall(s)))

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])