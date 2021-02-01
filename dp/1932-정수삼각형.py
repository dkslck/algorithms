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
    n = int(input().strip())
    mat = [None for _ in range(n)]
    for i in range(n):
        l = [int(i) for i in input().split()]
        mat[i] = l
    
    global dp
    dp = [[None for _ in range(n)] for _ in range(n)]
    buildDP(mat)

    ans = solve(mat)
    print(ans)

def buildDP(mat):
    global dp
    dp[0][0] = mat[0][0]
    for i in range(1, len(mat)):
        l = len(mat[i])
        for j in range(l):
            if j == 0:
                dp[i][j] = mat[i][j] + dp[i-1][j]
                continue
            if j == l-1:
                dp[i][j] = mat[i][j] + dp[i-1][j-1]
                continue
            dp[i][j] = mat[i][j] + max(dp[i-1][j], dp[i-1][j-1])

def solve(mat):
    global dp
    buildDP(mat)
    return max(dp[-1])



if __name__ == "__main__":
    main()
