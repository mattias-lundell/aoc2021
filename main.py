import time
import math


def run(day, year=2021):
    print(f"AOC {year} Day {day}")
    print()

    padded_day = str(day).zfill(2)

    mod = __import__(padded_day)
    data = None
    res1, res2, test_data = get_data(f'{padded_day}.test')
    print(res1)
    print(res2)
    print(test_data)

    test_1_res, _ = run_part(1, mod, test_data)
    if test_1_res == res1:
        data = get_data(f'{padded_day}.txt')
        res, time = run_part(1, mod, data)
        print_execution(1, res, time)
    else:
        print(f'fail test 1: was {test_1_res} expected {res1}')
        return
    test_2_res, _ = run_part(2, mod, test_data)
    if test_2_res == res2:
        res, time = run_part(2, mod, data)
        print_execution(2, res, time)
    else:
        print(f'fail test 2: was {test_2_res} expected {res2}')


def print_execution(part, res, time):
    print(f"Part {part}")
    print(f"Output: {res}")
    print(f"Output: {time:.4f}ms")
    print()


def get_data(fname):
    try:
        with open(fname, 'r') as f:

            res1 = f.readline().strip()
            res2 = f.readline().strip()
            data = f.read().strip()

            print(int(res1) == 10)
            return int(res1), res2, data


        # with open(fname, "r") as f:
        #     return [l.strip() for l in f.readlines()]
    except Exception as e:
        raise ValueError(f"Unable to read file {fname}") from e


def run_part(part, mod, data):
    funcname = f'part{part}'

    prep = getattr(mod, 'prep', None)
    f = getattr(mod, funcname, None)
    if callable(f):
        data = prep(data)
        t0 = time.perf_counter()
        val = f(data)
        t1 = time.perf_counter()
        return val, (t1 - t0) * 1000

    print(f"No {funcname} function")
    return None, 0


import sys

run(int(sys.argv[1]))
