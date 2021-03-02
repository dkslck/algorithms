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

    global N, mat, isTeam1
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    isTeam1 = [False] * N

    # ######## INPUT AREA END ############
    # ####################################

    global diff, s1, s2
    diff = 10 ** 9
    s1 = 0
    s2 = 0

    dfs(0, 0)
    print(diff)


def dfs(idx, num):
    if idx == N:
        return
    if num == N // 2:
        calculate()
        return
    isTeam1[idx] = True
    dfs(idx + 1, num+1)
    isTeam1[idx] = False
    dfs(idx + 1, num)


def calculate():
    team1 = []
    team2 = []
    for i, e in enu(isTeam1):
        if e:
            team1.append(i)
        else:
            team2.append(i)


    t1Score = 0
    t2Score = 0
    for x, y in product(team1, repeat=2):
        t1Score += mat[x][y]

    for x, y in product(team2, repeat=2):
        t2Score += mat[x][y]

    d = abs(t1Score - t2Score)
    global diff, s1, s2
    if d < diff:
        diff = d
        s1 = t1Score
        s2 = t2Score






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
