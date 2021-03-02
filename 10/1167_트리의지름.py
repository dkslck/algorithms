import os
import sys
import itertools
import collections

def main(f = None):
    init(f)
    
    n = int(input())
    edges = [[] for _ in range(n+1)]

    for _ in range(n):
        arr = list(map(int, input().split()))
        from_ = arr[0]
        for i in range(1, len(arr)-2, 2):
            to = arr[i]
            d = arr[i+1]
            edges[from_].append((to, d))

    root = 1
    g = Graph(edges)
    x, d = g.getFarNode(root)
    y, d = g.getFarNode(x)
    print(d)



class Graph:
    def __init__(s, edges):
        s.e = edges
        s.n = len(edges)

    def getFarNode(s, from_):
        n = s.n
        vis = [False for _ in range(n)]
        distance = [-100 for _ in range(n)]

        s.bfs(vis, distance, 0, from_)

        idx = distance.index(max(distance))
        return idx, distance[idx]

    def bfs(s, vis, distance, dist, from_):
        dq = collections.deque()
        vis[from_] = True
        dq.append((from_, dist))
        while dq:
            f, d = dq.popleft()
            distance[f] = d
            for node, dis in s.e[f]:
                if not vis[node]:
                    vis[node] = True
                    dq.append((node, dis + d))
    

    
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



if __name__ == "__main__":
    main()
