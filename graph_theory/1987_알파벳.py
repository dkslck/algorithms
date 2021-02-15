# CP template Version 1.006
import os
import sys
import itertools
DEBUG = False


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dx = [-1, 1, 0 ,0]
dy = [0, 0, 1, -1]
def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ####################################
    # ######## INPUT AREA BEGIN ##########

    R, C = map(int, input().split())
    mat = [list(input().strip()) for _ in range(R)]

    # ######## INPUT AREA END ############
    # ####################################
    base = ord('A')
    for i, j in For(R, C):
        mat[i][j] = ord(mat[i][j]) - base

    check = Mat(R, C, 0)

    stack = []
    maxCount = 0
    mask = 1 << mat[0][0]
    stack.append((0, 0, mask, 1))
    check[0][0] = mask
    while stack:
        i, j, visited, count = stack.pop()
        maxCount = max(maxCount, count)
        for n in range(4):
            ni = i + dx[n]
            nj = j + dy[n]

            if 0 <= ni < R and 0 <= nj < C:
                val = 1 << mat[ni][nj]
                nMask = visited | val
                if visited != nMask:
                    if check[ni][nj] != nMask:
                        check[ni][nj] = nMask
                        stack.append((ni, nj, nMask, count + 1))

    print(maxCount)



enu = enumerate


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



if __name__ == "__main__":
    main()
