from collections import Counter, defaultdict
from functools import cache
import itertools
import math as m
import math

test = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


def part1(data):
    return len(backtrack(data, 'start', 'end', set(), list(), list()))


def backtrack(g, s, e, visited, path, paths):
    visited.add(s)
    path.append(s)

    if s == e:
        paths.append(path[:])
    else:
        for i in g[s]:
            if i.isupper() or i not in visited:
                backtrack(g, i, e, visited, path, paths)

    path.pop()
    visited.discard(s)

    return paths


def part2(data):
    return len(backtrack2(data, 'start', 'end', set(), list(), list(), False))


def backtrack2(g, s, e, visited, path, paths, revisited):
    visited.add(s)
    path.append(s)

    if s == e:
        paths.append(path[:])
    else:
        for i in g[s]:
            if i.isupper():
                backtrack2(g, i, e, visited.copy(), path[:] , paths, revisited)
            elif i not in visited:
                backtrack2(g, i, e, visited.copy(), path[:], paths, revisited)
            elif i in visited and not revisited:
                backtrack2(g, i, e, visited.copy(), path[:], paths, True)

    path.pop()
    visited.discard(s)

    return paths


def prep(data):
    g = defaultdict(list)
    for i, row in enumerate(data.split('\n')):
        print(row)
        a, b = row.split('-')[:2]
        if b != 'start':
            g[a].append(b)
        if b != 'end' and a != 'start' :
            g[b].append(a)
    return g


if __name__ == '__main__':
    print("part1 test", part1(prep(test)))
    print("part1 real", part1(prep(open('in12.txt').read())))
    print("part2 test", part2(prep(test)))
    print("part2 real", part2(prep(open('in12.txt').read())))
