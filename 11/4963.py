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
    while True:
        w, h = (int(i) for i in input().split())
        if w == h == 0:
            return
        mat = [list(map(int, input().split())) for _ in range(h)]

        count = 0
        for i in range(h):
            for j in range(w):
                if mat[i][j] == 1:
                    count += 1
                    dfs(mat, w, h, i, j)
        print(count)

def dfs(mat, w, h, i, j):
    if not 0 <= i < h:
        return
    if not 0 <= j < w:
        return
    if mat[i][j] == 0:
        return
    mat[i][j] = 0

    for x, y in itertools.product([-1, 0, 1], repeat = 2):
        dfs(mat, w, h, i+x, j+y)


if __name__ == "__main__":
    main()
