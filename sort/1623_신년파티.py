

def For(*args):
    return itertools.product(*map(range, args))

def copy2d(mat):
    return [row[:] for row in mat]

def Mat(h, w, default = None):
    return [[default for _ in range(w)] for _ in range(h)]

# CP template Version 1.005
import os
import sys
sys.setrecursionlimit(10**9)

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

def pfast(*args, end = "\n", sep=' '): sys.stdout.write(sep.join(map(str, args)) + end)

def parr(arr):
    for i in arr:
        print(i)

input = sys.stdin.readline # by default

def dfs(cur):
    for child in tree[cur]:
        dfs(child)
    
    if not tree[cur]:
        cache[cur][0] = 0
        cache[cur][1] = cost[cur]
    else:
        cache[cur][0] = sum(list(max(cache[x]) for x in tree[cur]))
        cache[cur][1] = cost[cur] + sum(cache[x][0] for x in tree[cur])

def sol(cur, flag):
    val = cache[cur][flag]
    if val != -1: return val
    val = 0

    if flag:
        val += cost[cur]
        for nxt in tree[cur]:
            val += sol(nxt, 0)
    
    else:
        for nxt in tree[cur]:
            val += max(sol(nxt, 0), sol(nxt, 1))
    cache[cur][flag] = val
    return val

def bt(cur, flag):
    global lst
    if flag:
        for nxt in tree[cur]:
            bt(nxt, 0)
    else:
        for nxt in tree[cur]:
            if cache[nxt][0] > cache[nxt][1]:
                bt(nxt, 0)
            else:
                bt(nxt, 1)
                lst.append(nxt+1)

def main(f):
    init(f)
    global tree, cache, cost, lst

    N = int(input())
    tree = [[] for _ in range(N)]
    cost = [int(i) for i in input().split()]
    parentOf = [None] + [int(i)-1 for i in input().split()]
    for i in range(1, N):
        tree[parentOf[i]].append(i)
    del parentOf
    cache = [[-1]*2 for _ in range(N)]
    dfs(0)
    #print(sol(0, 1), sol(0, 0))
    print(cache[0][1], cache[0][0])
    del cost
    lst = [1]
    bt(0, 1)
    lst.sort()
    pfast(*lst, -1)

    lst = []
    bt(0, 0)
    lst.sort()
    pfast(*lst, -1)

if __name__ == "__main__":
    main(None)
