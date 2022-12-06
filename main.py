import argparse
import os
import sys
import importlib
from timeit import timeit
import time
from datetime import datetime, timezone, timedelta
from copy import deepcopy

from dotenv import load_dotenv

import aocd
from aocd.models import Puzzle

load_dotenv()

today = datetime.now(timezone(-timedelta(hours=5))) # EST
if today.month != 12:
    pass

parser = argparse.ArgumentParser()
parser.add_argument('--year', '-y', nargs='?', default=today.year, type=int)
parser.add_argument('--day', '-d', nargs='?', default=[None,today.day][today.month == 12], type=int)
parser.add_argument('--create', '-c', action='store_true', help="Just creates the folder")
parser.add_argument('--testing', '-t', action='store_true', help="Only run dummy.txt")

arguments = parser.parse_args()

def create_day(directory, flags, puzzle):
    """Creates the directory if it doesn't exist."""

    if not os.path.exists(directory):
        print(f"Creating directory: {directory}")
        os.mkdir(directory)

    if not os.path.exists(f:=os.path.join(directory, 'solution.py')):
        with open(f, "w", encoding='utf-8') as f:
            f.write(f"""\"\"\"
Day {str(flags.day).zfill(2)}: {puzzle.title}

Part 1: 
Part 2: 
\"\"\"

def parse_data(f):
    return f.read().splitlines()

def part1(data):
    pass

def part2(data):
    pass
""") # Generate template

    try:
        with open(os.path.join(directory, 'data.txt'), "w", encoding='utf-8') as f: # aocd caches so no unnecessary requests done
            f.write(puzzle.input_data)
    except Exception as e:
        print(e)

    try:
        if not os.path.exists(f:=os.path.join(directory, 'dummy.txt')):
            with open(f, "w", encoding='utf-8') as f:
                f.write(puzzle.example_data)
    except Exception as e:
        print(e)


def format_time(dt): # https://github.com/python/cpython/blob/main/Lib/timeit.py#L339-L351
    units = {"nsec": 1e-9, "usec": 1e-6, "msec": 1e-3, "sec": 1.0}

    scales = [(scale, unit) for unit, scale in units.items()]
    scales.sort(reverse=True)
    for scale, unit in scales:
        if dt >= scale:
            break

    return "%.*g %s" % (3, dt / scale, unit)

puzzle = Puzzle(arguments.year, arguments.day)

if arguments.create:
    assert arguments.year > 2015
    assert 0 < arguments.day < 26

    dir_ = os.path.join(os.getcwd(), str(arguments.year), 'day' + str(arguments.day).zfill(2))
    create_day(dir_, arguments, puzzle)
elif 0 < arguments.day < 26:
    dir_ = os.path.join(os.getcwd(), str(arguments.year), 'day' + str(arguments.day).zfill(2))
    create_day(dir_, arguments, puzzle)
    file = os.path.join(dir_, 'solution.py')

    print("Running Year", arguments.year, 'Day', arguments.day, ' - ', file)
    print()

    spec = importlib.util.spec_from_file_location('solution', file)
    sol = importlib.util.module_from_spec(spec)
    sys.modules['solution'] = sol
    spec.loader.exec_module(sol)
    parse_data = sol.parse_data
    part1 = sol.part1
    part2 = sol.part2

    print("Dummy Data")
    with open(os.path.join(dir_, 'dummy.txt'), "r", encoding='utf-8') as f:
        data = parse_data(f)

    start = time.time()
    ans1 = part1(deepcopy(data))
    time1 = time.time() - start
    print("Part 1:", ans1, "- Timing:", format_time(time1))

    start = time.time()
    ans2 = part2(deepcopy(data))
    time2 = time.time() - start
    print("Part 2:", ans2, "- Timing:", format_time(time2))

    if not arguments.testing:
        print("\nReal Data")
        with open(os.path.join(dir_, 'data.txt'), "r", encoding='utf-8') as f:
            data = parse_data(f)

        start = time.time()
        ans1 = part1(deepcopy(data))
        time1 = time.time() - start
        try:
            solved1 = puzzle._get_answer('a')
        except aocd.exceptions.PuzzleUnsolvedError:
            solved1 = None
        print("Part 1:", ans1, "- Timing:", format_time(time1), ["❌", "✅"][str(solved1) == str(ans1)])

        start = time.time()
        ans2 = part2(deepcopy(data))
        time2 = time.time() - start
        try:
            solved2 = puzzle._get_answer('b')
        except aocd.exceptions.PuzzleUnsolvedError:
            solved2 = None
        print("Part 2:", ans2, "- Timing:", format_time(time2), ["❌", "✅"][str(solved2) == str(ans2)])
else:
    raise Exception("Day flag must be specified")
