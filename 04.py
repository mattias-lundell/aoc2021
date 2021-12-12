from collections import Counter
import itertools

test = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


def part1(numbers, boards):
    for i in range(5, len(numbers)):
        ns = set(numbers[:i])
        for board in boards:
            if bingo(ns, board):
                return numbers[i-1] * sum(elem for elem in itertools.chain(*board[0]) if elem not in numbers[:i])


def bingo(numbers, board):
    rows, cols = board

    return any(all_match(numbers, col) for col in cols) or any(all_match(numbers, row) for row in rows)


def all_match(numbers, row):
    return row.issubset(numbers)


def transpose(xs):
    return list(map(list, zip(*xs)))


def part2(numbers, boards):
    for i in range(5, len(numbers)):
        ns = set(numbers[:i])
        for board in boards:
            if bingo(ns, board):
                if len(boards) == 1:
                    return numbers[i-1] * sum(elem for elem in itertools.chain(*board[0]) if elem not in numbers[:i])
                boards.remove(board)
                return part2(numbers, boards)


def prep(data):
    lines = data.split('\n\n')
    numbers = [int(a) for a in lines[0].split(',')]
    boards = [[[int(c) for c in b.split()] for b in a.split('\n')] for a in lines[1:]]
    boards = [([set(a) for a in board], [set(a) for a in transpose(board)]) for board in boards]

    return numbers, boards


if __name__ == '__main__':
    print("part1 test", part1(*prep(test)))
    print("part1 real", part1(*prep(open('in04.txt').read())))
    print("part2 test", part2(*prep(test)))
    print("part2 real", part2(*prep(open('in04.txt').read())))
