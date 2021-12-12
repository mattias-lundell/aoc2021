from collections import Counter

test = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def part1(lines):
    lines = transpose(lines)
    gamma = int("".join([Counter(xs).most_common()[0][0] for xs in lines]), 2)
    epsilon = int("".join([Counter(xs).most_common()[-1][0] for xs in lines]), 2)

    return gamma*epsilon


def transpose(xs):
    return list(map(list, zip(*xs)))


def part2(lines):
    transposed = transpose(lines)
    oxygen = lines
    for i, xs in enumerate(transposed):
        c = most_common(transpose(oxygen)[i])
        oxygen = [x for x in oxygen if x[i] == c]
    oxygen = int("".join(oxygen), 2)

    co2 = lines
    for i, xs in enumerate(transposed):
        c = least_common(transpose(co2)[i])
        co2 = [x for x in co2 if x[i] == c]
    co2 = int("".join(co2), 2)

    return oxygen*co2


def most_common(xs):
    if len(xs) == 1:
        return xs[0]
    cnt = Counter(xs).most_common()
    if cnt[0][1] == cnt[-1][1]:
        return '1'
    return cnt[0][0]


def least_common(xs):
    if len(xs) == 1:
        return xs[0]
    cnt = Counter(xs).most_common()
    if cnt[0][1] == cnt[-1][1]:
        return '0'
    return cnt[-1][0]


if __name__ == '__main__':
    print("part1 test", part1(test.splitlines()))
    print("part1 real", part1(open('in03.txt').readlines()))
    print("part2 test", part2(test.splitlines()))
    print("part2 real", part2(open('in03.txt').readlines()))
