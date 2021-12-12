from collections import Counter, defaultdict
from functools import cache
import itertools
import math as m
import math

test = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


def part1(data):
    s = 0
    for row in data:
        q = []
        for c in row:
            if c in {'(', '[', '{', '<'}:
                q.append(c)
            else:
                cc = q.pop()
                if c != match(cc):
                    s += {')': 3, ']': 57, '}': 1197, '>': 25137}[c]
    return s

def match(c):
    return {'(': ')', '[': ']', '{': '}', '<': '>',
            ')': '(', ']': '[', '}': '{', '>': '<'}[c]


def part2(data):
    scores = []
    for row in data:
        score = repair(row)
        if score > 0:
            scores.append(score)
    return sorted(scores)[int(len(scores)/2)]

def repair(row):
    q = []
    for c in row:
        if c in {'(', '[', '{', '<'}:
            q.append(c)
        else:
            cc = q.pop()
            if c != match(cc):
                return 0
    return cost(q)


def cost(row):
    s = 0
    for c in reversed(row):
        s = s * 5 + {')': 1, ']': 2, '}': 3, '>': 4}[match(c)]
    return s


def prep(data):
    return data.split('\n')


if __name__ == '__main__':
    print("part1 test", part1(prep(test)))
    print("part1 real", part1(prep(open('in10.txt').read())))
    print("part2 test", part2(prep(test)))
    print("part2 real", part2(prep(open('in10.txt').read())))
