import os
import sys
import itertools
import collections

sys.setrecursionlimit(1500)

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


def LCS(S1, S2, i, j):
    global dp
    def LCS_(i, j):
        return LCS(S1, S2, i, j)
    if dp[i][j] is not None: return dp[i][j]

    if i == 0:
        val = 1 if S1[i] == S2[j] else LCS_(i, j-1)
        dp[i][j] = val
        return val
    if j == 0:
        val = 1 if S1[i] == S2[j] else LCS_(i-1, j)
        dp[i][j] = val
        return val

    if S1[i] == S2[j]:
        dp[i][j] = LCS_(i-1, j-1) + 1
    else:
        left = LCS_(i-1, j)
        right = LCS_(i, j-1)
        dp[i][j] = max(left, right)
    return dp[i][j]

def solve(S1, S2):
    global dp
    l1 = len(S1)
    l2 = len(S2)
    dp[0][0] = 1 if S1[0] == S2[0] else 0
    for i in range(l1-1):
        for j in range(l2-1):
            LCS(S1, S2, i, j)

    ans = LCS(S1, S2, l1-1, l2-1)
    return ans

def main(f = None):
    init(f)
    global dp
    dp = [[None for _ in range(1001)] for _ in range(1001)]
    S1 = input().strip()
    S2 = input().strip()
    ans = solve(S1, S2)
    print(ans)

if __name__ == "__main__":
    main()
