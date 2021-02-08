import os
import sys
import itertools
import collections


def solve(mat):
    n = len(mat)
    for i in range(n):
        mat[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                mat[i][j] = min(mat[i][k] + mat[k][j], mat[i][j])
            


def main(f = None):
    init(f)
    n = int(input().strip())
    m = int(input().strip())

    mat = [[float("inf") for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b, c = (int(i) for i in input().split())
        a = a-1
        b = b-1
        mat[a][b] = min(mat[a][b], c)

    solve(mat)


    for i in range(n):
        for j in range(n):
            a = mat[i][j]
            if a == float("inf"):
                a = 0
            print(a, end=' ')
        print()



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


def prmat(mat):
    for i in mat:
        print(i)

        


if __name__ == "__main__":
    main()
