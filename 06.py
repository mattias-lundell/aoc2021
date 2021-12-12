from collections import Counter, defaultdict
import itertools
import math as m
test = """3,4,3,1,2"""


def part1(data, daymax=80):
    for day in range(daymax):
        n = []
        for i in range(len(data)):
            if data[i] == 0:
                data[i] = 6
                n.append(8)
            else:
                data[i] -= 1
        data.extend(n)
    return len(data)


def part2(_data, daymax=80):
    data = defaultdict(int)
    for d in _data:
        data[d] += 1
    for day in range(daymax):
        new = defaultdict(int)
        new[8] = data[0]
        new[6] += data[0]
        for i in range(1, 9):
            new[i-1] += data.get(i, 0)
        data = new

    return sum(data.values())


def prep(data):
    return [int(x) for x in data.split(',')]


if __name__ == '__main__':
    print("part1 test", part2(prep(test), daymax=80))
    print("part1 real", part2(prep(open('in06.txt').read())))
    print("part2 test", part2(prep(test), daymax=256))
    print("part2 real", part2(prep(open('in06.txt').read()), daymax=256))
