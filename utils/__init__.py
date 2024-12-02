"""
Utils Module to quickly work with common concepts.
"""

from .grid import Grid
from .maze import Maze
import re

number_re = re.compile(r'-?\d+')

def get_numbers(s):
    return list(map(int, number_re.findall(s)))