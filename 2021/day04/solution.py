"""
Day 04: Giant Squid

Part 1: 
Part 2: 
"""

def parse_data(f):
    numbers, *boards = f.read().split('\n\n')
    numbers = list(map(int, numbers.split(',')))
    boards_ = boards

    boards = [[{int(c): False for c in b.split()} for b in a.splitlines()] for a in boards]
    boards_ = [[{int(c): True for c in b.split()} for b in a.splitlines()] for a in boards_]

    return numbers, boards, boards_

def part1(data):
    nums, boards, _ = data

    hasWon = False
    num = 0
    for num in nums:
        for b, board in enumerate(boards):
            for i, row in enumerate(board):
                for col in row:
                    if col == num:
                        board[i][col] = True

            for row in board:
                if all(row.values()):
                    hasWon = b, num

            zippedBoard = list(zip(*[a.values() for a in board]))
            if any(all(a) for a in zippedBoard):
                hasWon = hasWon or b, num

            if hasWon:
                break

        if hasWon:
            break

    board = boards[hasWon[0]]
    total = 0
    for row in board:
        for col, didshow in row.items():
            total += col * (not didshow)

    return num * total


def part2(data):
    nums, _, boards = data

    hasWon = False
    num = 0 # no more lint error hehe
    for num in nums[::-1]:
        for b, board in enumerate(boards):
            for i, row in enumerate(board):
                for col in row:
                    if col == num:
                        board[i][col] = False

            zippedBoard = list(zip(*[a.values() for a in board]))
            if not (any(all(a) for a in zippedBoard) or any(all(p.values()) for p in board)):
                hasWon = b, num

            if hasWon:
                break

        if hasWon:
            break

    board = boards[hasWon[0]]
    total = 0
    for row in board:
        for col, didshow in row.items():
            total += col * (not didshow)

    return num * (total - num)
