def main(f = None):
    global arr
    init(f)
    #sys.setrecursionlimit(10**9)

    ######################################
    ########## input area begin ##########

    N, C = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    arr.sort() # O(NlogN)

    ########## input area end ############
    ######################################

    maxDistance = max(arr)
    n = binRight(arr, C, 1, maxDistance, install)
    print(n-1)

def install(distance):
    """
    returns how many routers one can install if a minimum distance between
    each router is given.
    """

    previousRouter = arr[0]
    cnt = 1
    for i in arr:
        if i - previousRouter >= distance: # once a router is installed
            previousRouter = i # log its location
            cnt += 1 # increase the number of routers installed
    return cnt

# Unused
def binLeft(arr, val, left, right, func):
    if left == right:
        return left
    
    mid = (left + right) // 2
    midVal = func(mid)
    if val >= midVal:
        return binLeft(arr, val, left, mid, func)
    else:
        return binLeft(arr, val, mid+1, right, func)

# O(N) * O(log N) == O(N log N) ?
def binRight(arr, val, left, right, func):
    if left == right:
        return left
    
    mid = (left + right)//2
    midVal = func(mid) # O(N)
    if val <= midVal:
        return binRight(arr, val, mid+1, right, func)
    else:
        return binRight(arr, val, left, mid, func)

################################################################################
################################################################################
################################ TEMPLATE AREA #################################
################################################################################
################################################################################

def argmax(arr):
    return max(enumerate(arr), key = lambda x:x[1])
def argmin(arr):
    return min(enumerate(arr), key = lambda x:x[1])

def For(*args):
    return itertools.product(*map(range, args))

def copy2d(mat):
    return [row[:] for row in mat]

def Mat(h, w, default = None):
    return [[default for _ in range(w)] for _ in range(h)]

def nDim(*args, default = None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default = default) for _ in range(args[0])]

# CP template Version 1.005
import os
import sys
import itertools
import collections
from functools import cmp_to_key
from itertools import product
from collections import deque, Counter, defaultdict as dd
from math import log, log2, ceil, floor, gcd, sqrt
import math
from heapq import heappush, heappop
from bisect import bisect_left as bl, bisect_right as br

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
