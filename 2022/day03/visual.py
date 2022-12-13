from blessed import Terminal
import time

ABC = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def draw_splitter(term):
    with term.location(term.width // 2 + 1, 22):
        print("|")
    with term.location(term.width // 2, 23):
        print("/ \\")

def move_line_down(term, first, second, row, delay, total):
    while row < 22:
        row += 1
        with term.location(term.width // 2 + 2 - len(first), row - 1):
            print(term.clear_eol + term.clear_bol)
        with term.location(term.width // 2 + 2 - len(first), row):
            print(term.clear_eol + term.clear_bol + first + second)
        time.sleep(delay)
    
    for i in range(3):
        with term.location(term.width // 2 - len(first), row + i):
            print(term.clear_eol + term.clear_bol)
        with term.location(term.width // 2 - len(first) - 3, row + i + 1):
            print(term.clear_eol + term.clear_bol + first + '          ' + second)
        draw_splitter(term)
        draw_pipes(term, i)

        time.sleep(delay)
    
    for i in range(3, 13):
        draw_splitter(term)
        draw_pipes(term, i)

        time.sleep(delay)
    
    draw_pipes(term, 0) # reset

    inter = list(set(first) & set(second))

    foo = ", ".join(inter)
    with term.location(term.width // 2 + 1 - len(foo) // 2, 36):
        print(term.clear_eol + term.clear_bol + foo)
        draw_counter(term, total)
    
    for i in range(4):
        draw_counter(term, total)
        with term.location(term.width // 2 - (3-i) - len(foo) // 2, 36):
            print(term.clear_eol + "-" + " " * (3-i) + foo + " " * (3-i) + "-")
        time.sleep(delay)
    
    foo = " + ".join(str(ABC.index(a)) for a in inter)
    with term.location(term.width // 2 + 1 - len(foo) // 2, 36):
        draw_counter(term, total)
        print(term.clear_eol + foo)
    
    
    total_ = 0
    for j in inter:
        total_ += ABC.index(j)
    return total_

def draw_counter(term, total):
    with term.location(term.width // 2 - 30, 36):
        print(term.clear_eol + term.on_yellow + term.blue + " Common Letters sum: " + str(total) + " " + term.normal)

def draw_pipes(term, row): # I know it's messy, shuddup
    print(term.move_xy(term.width // 2 - 13, 22))
    print(rf"""
{term.clear_eol}{' ' * (term.width // 2 - 20)}{['', term.on_green][row == 1] }\                  /   \                  /{term.normal}
{term.clear_eol}{' ' * (term.width // 2 - 20)} {['', term.on_green][row == 2] }\                /     \                /{term.normal}
{term.clear_eol}{' ' * (term.width // 2 - 20)}  {['', term.on_green][row == 3] }\              /       \              /{term.normal}
{term.clear_eol}{' ' * (term.width // 2 - 20)}   {['', term.on_green][row == 4] }\            /         \            /{term.normal}
{term.clear_eol}{' ' * (term.width // 2 - 20)}    {['', term.on_green][row == 5] }\          /           \          /{term.normal}
{term.clear_eol}{' ' * (term.width // 2 - 20)}     {['', term.on_green][row == 6] }\        /             \        /{term.normal}
{term.clear_eol}{' ' * (term.width // 2 - 20)}     {['', term.on_green][row == 7] }|       |               |       |{term.normal}
{term.clear_eol}{' ' * (term.width // 2 - 20)}      {['', term.on_green][row == 8] }\       \_____________/       /{term.normal}
{term.clear_eol}{' ' * (term.width // 2 - 20)}       {['', term.on_green][row == 9] }\                           /{term.normal}
{term.clear_eol}{' ' * (term.width // 2 - 20)}        {['', term.on_green][row == 10]}^-_______         _______-^{term.normal}
{term.clear_eol}{' ' * (term.width // 2 - 20)}                 {['', term.on_green][row == 11]}|       |{term.normal}
{term.clear_eol}{' ' * (term.width // 2 - 20)}                 {['', term.on_green][row == 12]}|       |{term.normal}
""")

def main(data, delay):
    lines = []
    for line in data:
        mid = len(line) // 2
        lines.append([line[:mid], line[mid:]])

    term = Terminal()

    print(term.normal + term.clear)

    for i, line in enumerate(lines):
        first, second = line
        with term.location(term.width // 2 - len(first) + 2, 20 - i):
            print(data[i])
    
    
    total = 0

    draw_splitter(term)
    draw_counter(term, total)
    draw_pipes(term, 0)

    input()

    for i, line in enumerate(lines):
        total += move_line_down(term, line[0], line[1], 20 - i, delay, total)
    
    time.sleep(delay*5)
    draw_counter(term, total)

    input()
    print(term.clear)