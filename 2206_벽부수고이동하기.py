# CP template Version 1.4
import os
import sys
import itertools
import collections
from functools import cmp_to_key
from itertools import product
from collections import deque, Counter
from math import log, ceil, floor

DEBUG = False

def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def init(f = None):
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

def main(f = None):
    init(f)
    n, m = (int(i) for i in  input().split())
    map = [[int(i) for i in input().strip()] for _ in range(n)]
    NoOne = 0
    UsedAbility = 1
    Naive = 2
    vis = [[NoOne for _ in range(m)] for _ in range(n)]

    arrival = (n-1, m-1)
    ans = -1

    dq = deque()
    vis[0][0] = Naive
    dq.append((0, 0, True, 1))

    while dq:
        i, j, canBreak, step = dq.popleft()
        if (i, j) == arrival:
            ans = step
            break

        lr = [1, 0, -1, 0]
        ud = [0, 1, 0, -1]

        for x, y in zip(lr, ud):
            iN, jN = i+x, j+y
            if 0 <= iN < n and 0 <= jN < m:
                visInfo = vis[iN][jN]
                if visInfo == NoOne:
                    if map[iN][jN] == 0:
                        if not canBreak:
                            vis[iN][jN] = UsedAbility
                        else:
                            vis[iN][jN] = Naive
                        dq.append((iN, jN, canBreak, step+1))
                    elif canBreak:
                        vis[iN][jN] = UsedAbility
                        dq.append((iN, jN, False, step+1))
                elif visInfo == UsedAbility:
                    if canBreak:
                        if map[iN][jN] == 0:
                            vis[iN][jN] = Naive
                            dq.append((iN, jN, True, step+1))
                            

    print(ans)





if __name__ == "__main__":
    main()
