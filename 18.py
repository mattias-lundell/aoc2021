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


def add(x, y):
    return _reduce((x, y))

def _reduce(n, d=1):
    if d == 4:
        a, b = n
        return (0, a+b)
    else:



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



'''
Ruby

My basic idea was to turn each snailfish number into an array of complex numbers a+bi, where a is the number and b is the depth (number of brackets the number is enclosed by). For example: [[[1, 2], 3], 4] would be encoded as [1+3i, 2+3i, 3+2i, 4+i]

def snail_parse(str)
  counter = 0
  output = []
  str.chars.each do |char|
    if char.match?(/\d/)
      output << char.to_i + counter.i
    elsif char == "["
      counter += 1
    elsif char == "]"
      counter -= 1
    end
  end
  output
end
Then, I know we have to explode any number where b >= 5 and split any number where a >= 10. So we can write methods to explode and split at a given index, and get the magnitude of a snailfish number:

def explode(arr, ind)
  first, second = arr.slice(ind, 2)
  arr[ind - 1] += first.real if ind != 0
  arr[ind + 2] += second.real if arr[ind + 2]
  arr.delete_at(ind)
  arr[ind] = 0 + (first.imaginary - 1).i
end

def split(arr, ind)
  arr.insert(ind + 1, (arr[ind].real / 2.0).round + (arr[ind].imaginary + 1).i)
  arr[ind] = arr[ind].real / 2 + (arr[ind].imaginary + 1).i
end

def get_magnitude(arr)
  loop do
    max_depth = arr.map(&:imaginary).max
    break if max_depth == 0
    ind = arr.index{ _1.imaginary == max_depth}
    arr[ind] = 3 * arr[ind].real + 2 * arr[ind + 1].real + (arr[ind].imaginary - 1).i
    arr.delete_at(ind + 1)
  end
  arr.first.real
end
Then we can add two snailfish numbers and loop until it's reduced:

def snail_add(a, b)
  joined = a.dup.concat(b).map{_1 + 1.i}
  loop do
    index_to_explode = joined.index{_1.imaginary >= 5}
    if index_to_explode
      explode(joined, index_to_explode) and next
    end
    index_to_split = joined.index{_1.real >= 10}
    if index_to_split
      split(joined, index_to_split) and next
    end
    break
  end
  joined
end
Now we can solve the problem with:

data = open("input").each_line.map{snail_parse(_1)}
puts get_magnitude(data.reduce{snail_add(_1, _2)}) # Part 1
p data.permutation(2).map{|a, b| get_magnitude(snail_add(a, b))}.max # Part 2

'''
