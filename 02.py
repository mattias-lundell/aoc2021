
test = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

def part1(lines):
    h = 0
    d = 0
    for line in lines:
        direction, delta = line.split()
        delta = int(delta)
        if direction == 'forward':
            h += delta
        elif direction == 'down':
            d += delta
        elif direction == 'up':
            d -= delta
    print(h*d)


def part2(lines):
    h = 0
    d = 0
    a = 0
    for line in lines:
        direction, delta = line.split()
        delta = int(delta)
        print(direction, delta)
        if direction == 'forward':
            h += delta
            d += (delta * a)
        elif direction == 'down':
            a += delta
        elif direction == 'up':
            a -= delta
    print(h*d)


if __name__ == '__main__':
    part1(test.splitlines())
    part1(open('in02.txt').readlines())
    part2(test.splitlines())
    part2(open('in02.txt').readlines())
