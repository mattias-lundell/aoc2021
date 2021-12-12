from collections import Counter, defaultdict
from functools import cache
import itertools
import math as m
import math

test = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def part1(data, steps):
    max_i = max([i for (i, _) in data])
    max_j = max([j for (_, j) in data])
    flashes = 0
    for s in range(steps):
        data, flashed = step(data)
        flashes += flashed

    return flashes


def pp(data, max_i, max_j):
    for i in range(max_i+1):
        print("".join(str(data[(i, j)]) for j in range(max_j+1)))
    print()


def step(data):
    for point in data:
        data[point] += 1

    return f(data, set())


def f(data, flashed):
    flash = False
    for point in data:
        if data[point] > 9 and point not in flashed:
            flash = True
            flashed.add(point)
            data[point] = 0
            for neighbour in adj(point, data):
                if neighbour not in flashed:
                    data[neighbour] += 1
    if flash:
        return f(data, flashed)
    else:
        return data, len(flashed)


def part2(data):
    max_i = max([i for (i, _) in data])
    max_j = max([j for (_, j) in data])
    i = 0
    while not synced(data):
        data, _ = step(data)
        i+=1

    return i


def synced(data):
    return sum(data.values()) == 0


def adj(point, data):
    i, j = point
    res = set()
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            else:
                pp = (i+di, j+dj)
                if pp in data:
                    res.add(pp)
    return res


def prep(data):
    res = dict()
    for i, row in enumerate(data.split('\n')):
        for j, energy in enumerate(row):
            res[(i, j)] = int(energy)
    return res


if __name__ == '__main__':
    print("part1 test", part1(prep(test), 100))
    print("part1 real", part1(prep(open('in11.txt').read()), 100))
    print("part2 test", part2(prep(test)))
    print("part2 real", part2(prep(open('in11.txt').read())))
