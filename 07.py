from collections import Counter, defaultdict
from functools import cache
import itertools
import math as m
test = """16,1,2,0,4,2,7,1,2,14"""


def part1(data):
    _max = max(data)
    _min = min(data)

    sums = []

    for i in range(_min, _max+1):
        sums.append(sum([abs(i-x) for x in data]))
    return min(sums)


def part2(data):
    _max = max(data)
    _min = min(data)

    sums = []

    for i in range(_min, _max+1):
        sums.append(sum([cost(max(i, x) - min(i, x)) for x in data]))
    return min(sums)


@cache
def cost(delta):
    return sum([i for i in range(delta+1)])


def prep(data):
    return [int(x) for x in data.split(',')]


if __name__ == '__main__':
    print("part1 test", part1(prep(test)))
    print("part1 real", part1(prep(open('in07.txt').read())))
    print("part2 test", part2(prep(test)))
    print("part2 real", part2(prep(open('in07.txt').read())))
