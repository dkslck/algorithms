# CP template Version 1.006
import os
import sys
import itertools
import collections
import string
# not for python < 3.9
# from functools import cmp_to_key, reduce, partial, cache
from functools import cmp_to_key, reduce, partial
from itertools import product
from collections import deque, Counter, defaultdict as dd
from math import log, log2, ceil, floor, gcd, sqrt
import math
from heapq import heappush, heappop
from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ####################################
    # ######## INPUT AREA BEGIN ##########
    global mat
    mat = Mat(3, 3)
    while True:
        line = input().strip()
        if line == "end": break
        arr = list(line)
        counter = Counter(arr)
        xCount = counter["X"]
        oCount = counter["O"]
        diff = xCount - oCount
        if not (diff == 0 or diff == 1):
            print("invalid")
            continue

        mat = []
        for i in range(0, 9, 3):
            mat.append(arr[i:i+3])

        xWin = isWinner('X')
        oWin = isWinner('O')
        if xWin and oWin:
            print("invalid")
            continue


        if xWin:
            if diff != 1:
                print("invalid")
                continue

        if oWin:
            if diff != 0:
                print("invalid")
                continue

        if not xWin and not oWin:
            if counter['.'] != 0:
                print("invalid")
                continue

        print("valid")


    # ######## INPUT AREA END ############
    # ####################################


def isWinner(char):
    for i in range(3):
        if mat[i][0] == mat[i][1] == mat[i][2] == char:
            return True

    for j in range(3):
        if mat[0][j] == mat[1][j] == mat[2][j] == char:
            return True

    if mat[0][0] == mat[1][1] == mat[2][2] == char:
        return True

    if mat[2][0] == mat[1][1] == mat[0][2] == char:
        return True

    return False


# #############################################################################
# #############################################################################
# ############################## TEMPLATE AREA ################################
# #############################################################################
# #############################################################################

enu = enumerate


def argmax(arr):
    return max(enumerate(arr), key=lambda x: x[1])


def argmin(arr):
    return min(enumerate(arr), key=lambda x: x[1])


def For(*args):
    return itertools.product(*map(range, args))


def copy2d(mat):
    return [row[:] for row in mat]


def Mat(h, w, default=None):
    return [[default for _ in range(w)] for _ in range(h)]


def nDim(*args, default=None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default=default) for _ in range(args[0])]


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline


def init(f=None):
    global input
    input = sys.stdin.readline  # by default
    if os.path.exists("o"):
        sys.stdout = open("o", "w")
    if f is not None:
        setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"):
                setStdin("in/i")
            elif os.path.isfile("i"):
                setStdin("i")
        elif len(sys.argv) == 2:
            setStdin(sys.argv[1])
        else:
            assert False, "Too many sys.argv: %d" % len(sys.argv)


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()
