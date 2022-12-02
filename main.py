import argparse
import os
import subprocess
import datetime

today = datetime.date.today()
if today.month != 12:
    pass

parser = argparse.ArgumentParser()
parser.add_argument('--year', '-y', nargs='?', default=today.year, type=int)
parser.add_argument('--day', '-d', nargs='?', default=[None,today.day][today.month == 12], type=int)
parser.add_argument('--create', '-c', action='store_true', help="Just creates or overwrites the folder")

arguments = parser.parse_args()

def create_day(directory):
    """Creates the directory if it doesn't exist."""
    if not os.path.exists(directory):
        print(f"Creating directory: {directory}")
        os.mkdir(directory)

    if not os.path.exists(f:=os.path.join(directory, 'solution.py')):
        with open(f, "w", encoding='utf-8') as f:
            f.write("""with open('data.txt', encoding='utf-8') as f:
    data = f.readlines()""") # Generate template
    if not os.path.exists(f:=os.path.join(directory, 'data.txt')):
        with open(f, "w", encoding='utf-8') as _:
            pass
    if not os.path.exists(f:=os.path.join(directory, 'dummy.txt')):
        with open(f, "w", encoding='utf-8') as _:
            pass


if arguments.create:
    assert arguments.year > 2015
    assert 0 < arguments.day < 26

    dir_ = os.path.join(os.getcwd(), str(arguments.year), 'day' + str(arguments.day).zfill(2))
    create_day(dir_)
elif 0 < arguments.day < 26:
    dir_ = os.path.join(os.getcwd(), str(arguments.year), 'day' + str(arguments.day).zfill(2))
    create_day(dir_)
    file = os.path.join(dir_, 'solution.py')

    print("Running Year", arguments.year, 'Day', arguments.day, ' - ', file)
    print()

    subprocess.call(['python', file], cwd=dir_)
else:
    raise Exception("Day flag must be specified")
