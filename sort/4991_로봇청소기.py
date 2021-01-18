def main(f = None):
    init(f)
    while True:
        w, h = map(int, input().split())
        if w == h == 0: return
        mat = [list(input().strip()) for _ in range(h)]

        start = None
        dirtyLocs = []

        for i, j in For(h, w):
            if mat[i][j] == 'o':
                start = (i, j)
            elif mat[i][j] == '*':
                dirtyLocs.append((i, j))
        numD = len(dirtyLocs)
        fStD = [None] * numD

        def getDistanceMatrix(start):
            si, sj = start
            dq = deque()
            dq.append((si, sj, 0))

            distance = Mat(h, w)
            distance[si][sj] = 0

            dx = (-1, 1, 0, 0)
            dy = (0, 0, -1, 1)

            while dq:
                i, j, d = dq.popleft()

                for x, y in zip(dx, dy):
                    ni, nj = i + x, j + y

                    if 0 <= ni < h and 0 <= nj < w:
                        if distance[ni][nj] is None:
                            if mat[ni][nj] != 'x':
                                distance[ni][nj] = d + 1
                                dq.append((ni, nj, d+1))
            return distance

        points = [start] + dirtyLocs
        nP = len(points)

        distMat = Mat(nP, nP)
        for i in range(nP):
            fx, fy = points[i]
            distMap = getDistanceMatrix((fx, fy))
            for j in range(i, nP):
                tx, ty = points[j]
                d = distMap[tx][ty]
                distMat[i][j] = d
                distMat[j][i] = d

        n = math.factorial(len(points)-1)
        perms = itertools.islice(itertools.permutations(range(len(points))), n)
        min_ = 987654321
        minPath = None
        for i in perms:
            path = list(i)
            sum_ = 0
            valid = True
            for i in range(len(path)-1):
                f = path[i]
                t = path[i+1]
                val = distMat[f][t]
                if val is None:
                    valid = False
                    break
                sum_ += distMat[f][t]
            if valid and min_ > sum_:
                min_ = sum_
                minPath = path
        if min_ != 987654321:
            print(min_)
        else:
            print(-1)








def Mat(h, w, default = None):
    return [[default for _ in range(w)] for _ in range(h)]

def For(*args):
    return itertools.product(*map(range, args))

def copy2d(mat):
    return [row[:] for row in mat]

# CP template Version 1.005
import os
import sys
import itertools
import collections
from functools import cmp_to_key
from itertools import product
from collections import deque, Counter
from math import log, log2, ceil, floor
import math
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right

DEBUG = False

def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline

def init(f = None):
    global input
    input = sys.stdin.readline # by default
    if os.path.exists("o"): sys.stdout = open("o", "w")
    if f is not None: setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"): setStdin("in/i")
            elif os.path.isfile("i"): setStdin("i")
        elif len(sys.argv) == 2: setStdin(sys.argv[1])
        else: assert False, "Too many sys.argv: %d" % len(sys.argv)

# Mod #
class Mod:
    MOD = 10**9 + 7
    maxN = 5
    FACT = [0] * maxN
    INV_FACT = [0] * maxN

    @staticmethod
    def setMOD(n): Mod.MOD = n

    @staticmethod
    def add(x, y): return (x+y) % Mod.MOD

    @staticmethod
    def multiply(x, y): return (x*y) % Mod.MOD

    @staticmethod
    def power(x, y):
        if y == 0: return 1
        elif y % 2: return Mod.multiply(x, Mod.power(x, y-1))
        else:
            a = Mod.power(x, y//2)
            return Mod.multiply(a, a)

    @staticmethod
    def inverse(x): return Mod.power(x, Mod.MOD-2)

    @staticmethod
    def divide(x, y): return Mod.multiply(x, Mod.inverse(y))

    @staticmethod
    def allFactorials():
        Mod.FACT[0] = 1
        for i in range(1, Mod.maxN): Mod.FACT[i] = Mod.multiply(i, Mod.FACT[i-1])

    @staticmethod
    def inverseFactorials():
        n = len(Mod.INV_FACT)
        Mod.INV_FACT[n-1] = Mod.inverse(Mod.FACT[n-1])
        for i in range(n-2, -1, -1): Mod.INV_FACT[i] = Mod.multiply(Mod.INV_FACT[i+1], i+1)

    @staticmethod
    def coeffBinom(n, k):
        if n < k: return 0
        return Mod.multiply(Mod.FACT[n], Mod.multiply(Mod.INV_FACT[k], Mod.INV_FACT[n-k]))
    
    @staticmethod
    def sum(it):
        res = 0
        for i in it: res = Mod.add(res, i)
        return res
# END Mod #

def dprint(*args):
    if DEBUG: print(*args)

def pfast(*args, end = "\n", sep=' '): sys.stdout.write(sep.join(map(str, args)) + end)

def parr(arr):
    for i in arr:
        print(i)

if __name__ == "__main__":
    main()
