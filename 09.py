from collections import Counter, defaultdict
from functools import cache
import itertools
import math as m
import math

test = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def part1(data):
    return sum(data[x]+1 for x in low_points(data))


def low_points(data):
    mins = set()
    for p in data:
        i, j = p
        mini = True
        for neighbour in adjvals(i, j, data):
            if neighbour <= data[p]:
                mini = False
                break
        if mini:
            mins.add(p)

    return mins


def adjvals(i, j, data):
    return [data[(x, y)] for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if (x, y) in data]


def adj(points, data):
    res = set()
    for (i, j) in points:
        res.update([(x, y) for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if (x, y) in data])
    return res


def part2(data):
    return math.prod(sorted([len(basin({low_point}, data)) for low_point in low_points(data)])[-3:])


def basin(points, data):
    new = {p for p in adj(points, data) if data[p] < 9 and p not in points}

    if len(new) == 0:
        return points.union(new)

    return basin(points.union(new), data)


def prep(data):
    rows = data.split('\n')
    res = {}
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            res[(i, j)] = int(val)

    return res


if __name__ == '__main__':
    print("part1 test", part1(prep(test)))
    print("part1 real", part1(prep(open('in09.txt').read())))
    print("part2 test", part2(prep(test)))
    print("part2 real", part2(prep(open('in09.txt').read())))
