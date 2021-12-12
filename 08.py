from collections import Counter, defaultdict
from functools import cache
import itertools
import math as m

test = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

'''

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

'''

def part1(data):
    s = set([2, 4, 3, 7])
    cnt = 0
    for _, a in data:
        cnt += sum(1 for x in a if len(x) in s)
    return cnt


def part2(data):
    s = 0

    for a, bb in data:
        b = defaultdict(list)
        for c in a:
            b[len(c)].append(set(list(c)))

        cf = b[2][0]
        acf = b[3][0]
        abcdefg = b[7][0]
        bcdf = b[4][0]


        a = acf - cf
        bdeg = abcdefg - acf
        bd = bcdf - cf
        eg = bdeg - bd
        acf = abcdefg - bdeg

        d1 = b[2][0]
        d4 = b[4][0]
        d7 = b[3][0]
        d8 = b[7][0]

        _a = d7-d1

        d0 = [c for c in b[6] if len(c - d4 - d7) == 2 and len(c - d7) == 3][0]

        _d = d8 - d0

        d9 = [c for c in b[6] if len(c - d4) != 3][0]

        _e = d8 - d9

        _g = d9 - d4 - _a

        _b = d4 - d1 - _d

        d3 = d7.union(_d).union(_g)

        d2 = [c for c in b[5] if len(c - d3 - d4) == 1][0]

        _f = d7 - d2

        # d6 = [c for c in b[6] if len(c - d3) == 2][0]

        d5 = _a.union(_b).union(_d).union(_f).union(_g)
        d6 = _a.union(_b).union(_d).union(_f).union(_g).union(_e)

        # print(_a, _b, _d, _e, _f, _g)
        # print(d0, d1, d2, d3, d4, d5, d6, d7, d8, d9)
        # 0 1 2 3 4 _ 6 7 8 9

        # a b _ d e f g

        ds = ["".join(sorted(d)) for d in [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]]

        s += int(''.join([str(ds.index(''.join(sorted(d)))) for d in bb]))

    return s


def prep(data):
    data = data.split('\n')
    data = [d.split('|') for d in data]
    data = [(x[0].strip().split(), x[1].strip().split()) for x in data]

    return data


if __name__ == '__main__':
    print("part1 test", part1(prep(test)))
    print("part1 real", part1(prep(open('in08.txt').read())))
    print("part2 test", part2(prep(test)))
    print("part2 real", part2(prep(open('in08.txt').read())))
