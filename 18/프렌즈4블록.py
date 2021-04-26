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

    # ######## INPUT AREA END ############
    # ####################################

    m = 4
    n = 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    ret = solution(m, n, board)
    print(ret)
    print(ret == 14)

dxy = ((0, 0), (0, 1), (1, 0), (1, 1))

def solution(m, n, board):
    b = [list(i) for i in board]
    parr(b)
    global count
    count = 0

    while True:
        changed = mark(m, n, b)
        if not changed:
            break
        input()
    return count

def mark(m, n, b):
    global count

    changed = False
    mat = Mat(m, n, False)
    for i in range(m-1):
        for j in range(n-1):
            val = b[i][j]
            for dx, dy in dxy:
                ni, nj = i + dx, j + dy
                if b[ni][nj] != val:
                    break
            else:
                changed = True
                count += 1
                for dx, dy in dxy:
                    ni, nj = i + dx, j + dy
                    mat[ni][nj] = True

    collapse(m, n, b, mat)
    return changed

def collapse(m, n, b, mat):
    for j in range(n):
        shift = 0
        for i in range(m-1, -1, -1):
            val = mat[i][j]
            mat[i][j] = shift
            if val:
                shift += 1
    print("before")
    parr(b)

    for j in range(n):
        for i in range(m-1, -1, -1):
            val = b[i][j]
            shift = mat[i][j]
            if shift == 0:
                continue
            b[i-shift][j] = val
            b[i][j] = None

    print("after")
    parr(mat)
    parr(b)










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
