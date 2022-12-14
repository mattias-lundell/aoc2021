from collections import Counter, defaultdict, deque
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
    return data


def part2(data):
    return data


def prep(data):
    return data.split('\n')


if __name__ == '__main__':
    print("part1 test", part1(prep(test)))
    print("part1 real", part1(prep(open('in10.txt').read())))
    print("part2 test", part2(prep(test)))
    print("part2 real", part2(prep(open('in10.txt').read())))
