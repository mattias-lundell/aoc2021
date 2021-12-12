from collections import Counter
import itertools
import math as m
test ="""0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


import time

def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print 'func:%r took: %2.4f sec' % \
          (f.__name__, te-ts)
        return result

    return timed

def part1(coords):
    covered = []
    for p0, p1 in coords:
        if p0[0] == p1[0]:
            covered.extend(cols(p0, p1))
        elif p0[1] == p1[1]:
            covered.extend(rows(p0, p1))
    cnt = Counter(covered)

    return len([cnt[a] for a in cnt if cnt[a] >= 2])


@timeit
def part2(coords):
    covered = []
    for p0, p1 in coords:
        if p0[0] == p1[0]:
            covered.extend(cols(p0, p1))
        elif p0[1] == p1[1]:
            covered.extend(rows(p0, p1))
        else:
            covered.extend(diags(p0, p1))
    cnt = Counter(covered)

    return len([cnt[a] for a in cnt if cnt[a] >= 2])


def cols(p0, p1):
    return [(p0[0], i) for i in range(min(p0[1], p1[1]), max(p0[1], p1[1])+1)]


def rows(p0, p1):
    return [(i, p0[1]) for i in range(min(p0[0], p1[0]), max(p0[0], p1[0])+1)]


def diags(p0, p1):
    (x0, y0), (x1, y1) = p0, p1
    dist = int(m.sqrt((x1 - x0)**2 + (y1 - y0)**2))
    dx = dy = 0
    if x1 > x0:
        dx = 1
        if y1 > y0:
            dy = 1
        else:
            dy = -1
    else:
        dx = -1
        if y1 > y0:
            dy = 1
        else:
            dy = -1

    covered = [(x0, y0)]
    for i in range(dist):
        x0 += dx
        y0 += dy
        covered.append((x0, y0))
        if (x0, y0) == (x1, y1):
            return covered


def prep(data):
    lines =[[tuple(map(int, y.split(','))) for y in x.split(' -> ')] for x in  data.split('\n')]
    lines =  [sorted(line, key=lambda tup: (tup[0],tup[1])) for line in lines]

    return lines


if __name__ == '__main__':
    print("part1 test", part1(prep(test)))
    print("part1 real", part1(prep(open('in05.txt').read())))
    print("part2 test", part2(prep(test)))
    print("part2 real", part2(prep(open('in05.txt').read())))
