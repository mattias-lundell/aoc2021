'''
s the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:

199
200
208
210
200
207
240
269
260
263
This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:
'''


test = [199,200,208,210,200,207,240,269,260,263]


def q0(ints):
    last = ints[0]
    n_increase = 0
    for current in ints[1:]:
        if current > last:
            n_increase += 1
        last = current
    return n_increase


def q1(ints):
    last = sum(ints[:3])
    n_increase = 0
    for idx in range(3,(len(ints))):
        current = sum(ints[idx-2:idx+1])
        if current > last:
            n_increase += 1
        last = current
    return n_increase


if __name__ == '__main__':
    in0 = [int(a.strip()) for a in open('in01.txt')]

    q0(test)
    q0(in0)
    print(q1(test))
    print(q1(in0))
