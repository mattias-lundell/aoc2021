from collections import Counter, defaultdict
from functools import cache
import itertools
import math as m
import math

test = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def part1(data):
    dots, folds = data

    new = set()

    d, at = folds[0]
    for (i, j) in dots:
        if d == 'x':
            if i > at:
                new.add((at - (i - at), j))
            else:
                new.add((i, j))
        if d == 'y':
            if j > at:
                new.add((i, at - (j - at)))
            else:
                new.add((i, j))
    pp(new)

    return len(new)


def pp(data):
    max_i = max([i for (i, _) in data])
    max_j = max([j for (_, j) in data])

    m = [ [" "]*(max_i+1) for j in range(max_j+1)]
    for i, j in data:
        m[j][i] = "X"

    for row in m:
        print("".join(row))
    print()


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
    dots, folds = data

    new = dots

    d, at = folds[0]
    for d, at in folds:
        new = set()
        for (i, j) in dots:
            if d == 'x':
                if i > at:
                    new.add((at - (i - at), j))
                else:
                    new.add((i, j))
            if d == 'y':
                if j > at:
                    new.add((i, at - (j - at)))
                else:
                    new.add((i, j))
        dots = new

    pp(new)

    return len(new)


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
    dots, folds = data.split('\n\n')
    dots = set([tuple(map(int, d.split(','))) for d in dots.split()])
    folds = [(f.split('=')[0][-1], int(f.split('=')[1])) for f in folds.split('\n')]
    return (dots, folds)


if __name__ == '__main__':
    print("part1 test", part1(prep(test)))
    print("part1 real", part1(prep(open('13.txt').read())))
    print("part2 test", part2(prep(test)))
    print("part2 real", part2(prep(open('13.txt').read())))
