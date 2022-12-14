from collections import Counter, defaultdict
from functools import cache
import itertools
import math as m
import math
import os

test = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def part1(data):
    return solve(data, 10)


def part2(data):
    return solve(data, 40)


def solve(data, steps):
    template, rules = data

    pair_counts = Counter(a+b for a, b in itertools.pairwise(template) if a+b in rules)
    counts = Counter(template)

    for i in range(steps):
        counts, pair_counts = step(rules, counts, pair_counts)

    res = counts.most_common()
    return res[0][1] - res[-1][1]


def step(rules, counts, pair_counts):
    new = Counter()
    for pair, count in pair_counts.items():
        if pair in rules:
            c = rules[pair]
            a, b = pair
            new[a+c] += count
            new[c+b] += count

            counts[c] += count

    return counts, new


def prep(data):
    template, rules = data.split('\n\n')
    rules = rules.split('\n')
    rules = {k: v  for k, v in [tuple(rule.split(' -> ')) for rule in rules]}

    return template, rules


if __name__ == '__main__':
    test_path = __file__.replace('.py', '.txt')

    print("part1 test", part1(prep(test)))
    print("part1 real", part1(prep(open(test_path).read())))
    print("part2 test", part2(prep(test)))
    print("part2 real", part2(prep(open(test_path).read())))
