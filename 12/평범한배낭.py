import os
import sys
import itertools
import collections

DEBUG = False

def setStdin(f):
    global DEBUG
    global input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def init(f = None):
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

def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)

def ints(): return map(int, sys.stdin.readline().rstrip().split())

def main(f = None):
    init(f)
    N, K = (int(i) for i in input().split())

    global dp
    dp = [[None for _ in range(K+1)] for _ in range(N)]
    items = [Item(*map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(K):
            knapsack(items, i, j)
    ans = knapsack(items, N-1, K)
    print(ans)


class Item:
    def __init__(s, w, v):
        s.w = w
        s.v = v
    
    def __repr__(s):
        return "Item:" + str((s.w, s.v))

def knapsack(items, i, K):
    item = items[i]

    if i == 0:
        if item.w <= K:
            return item.v
        else:
            return 0
    
    if dp[i][K] is not None:
        return dp[i][K]

    if item.w > K:
        ret = knapsack(items, i-1, K)
        dp[i][K] = ret
        return ret

    cand1 = knapsack(items, i-1, K - item.w) + item.v
    cand2 = knapsack(items, i-1, K)
    ret = max(cand1, cand2)
    dp[i][K] = ret
    return ret


if __name__ == "__main__":
    main()
