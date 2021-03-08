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

    global N, M, mat
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # ######## INPUT AREA END ############
    # ####################################

    global AIR
    AIR = 2
    for i in range(M):
        mat[0][i] = AIR
    for i in range(1, N-1):
        mat[i][0] = AIR
        mat[i][M-1] = AIR
    for i in range(M):
        mat[N-1][i] = AIR


    prevNumC = 0
    step = 0
    while True:
        numC = countC()
        if numC == 0:
            break

        fillAir()
        melt()

        step += 1
        prevNumC = numC
    print(step)
    print(prevNumC)





di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def fillAir():

    dq = deque()
    for i, j in For(N, M):
        if mat[i][j] == AIR:
            dq.append((i, j))

    while dq:
        i, j = dq.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < M:
                if mat[ni][nj] == 0:
                    mat[ni][nj] = 2
                    dq.append((ni, nj))


def melt():
    for i, j in For(N, M):
        if mat[i][j] == AIR:
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < M:
                    if mat[ni][nj] == 1:
                        mat[ni][nj] = 0


def countC():
    cnt = 0
    for i, j in For(N, M):
        if mat[i][j] == 1:
            cnt += 1
    return cnt



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
