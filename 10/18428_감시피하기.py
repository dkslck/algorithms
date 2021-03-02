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

    global N, mat, teacherLocs
    N = int(input())
    mat = [list(input().split()) for _ in range(N)]

    # ######## INPUT AREA END ############
    # ####################################

    teacherLocs = []
    for i, j in For(N, N):
        if mat[i][j] == 'T':
            teacherLocs.append((i, j))

    dfs(-1, 0, 0)
    print("NO")


def dfs(i, j, numObs):
    if numObs == 3:
        if check():
            print("YES")
            exit(0)
        else:
            return

    while True:
        i += 1
        if i == N:
            i = 0
            j += 1
        if j == N:
            break

        if mat[i][j] == 'X':
            mat[i][j] = 'O'
            dfs(i, j, numObs + 1)
            mat[i][j] = 'X'


def check():
    for i, j in teacherLocs:
        # up
        ni = i
        while True:
            ni -= 1
            if ni < 0:
                break
            if mat[ni][j] == 'O':
                break
            if mat[ni][j] == 'S':
                return False

        ni = i
        while True:
            ni += 1
            if ni >= N:
                break
            if mat[ni][j] == 'O':
                break
            if mat[ni][j] == 'S':
                return False

        nj = j
        while True:
            nj -= 1
            if nj < 0:
                break
            if mat[i][nj] == 'O':
                break
            if mat[i][nj] == 'S':
                return False

        nj = j
        while True:
            nj += 1
            if nj >= N:
                break
            if mat[i][nj] == 'O':
                break
            if mat[i][nj] == 'S':
                return False

    return True


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
