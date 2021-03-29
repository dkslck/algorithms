# CP template Version 1.006
import os
import sys
import itertools
import collections
import string
# not for python < 3.9
# from functools import cmp_to_key, reduce, partial, cache
from functools import cmp_to_key, reduce, partial
from itertools import product
from collections import deque, Counter, defaultdict as dd
from math import log, log2, ceil, floor, gcd, sqrt
import math
from heapq import heappush, heappop
from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ####################################
    # ######## INPUT AREA BEGIN ##########

    jobs = [[0,3], [1, 9], [2, 6]]
    jobs.sort()
    ans = solution(jobs)
    assert ans == 9

    # ######## INPUT AREA END ############
    # ####################################

def solution(jobs):
    jq = jobQueue(jobs)
    jq.run()
    answer = jq.computeAvg()
    print(answer)
    return answer


class jobQueue:
    def __init__(self, jobs):
        self.jobs = jobs
        self.pq = []
        self.time = 0
        self.jobIdxToBeAdded = 0
        self.sum = 0
        self.completedJobs = 0

    def run(self):
        while True:
            self.addJobs()
            notIdle = self.executeJob()
            if not self.pq and self.jobIdxToBeAdded == len(self.jobs):
                break

    def addJobs(self):
        while self.jobIdxToBeAdded < len(self.jobs):
            if self.jobs[self.jobIdxToBeAdded][0] > self.time:
                return
            heappush(self.pq, (self.jobs[self.jobIdxToBeAdded][1], self.jobs[self.jobIdxToBeAdded][0], self.jobIdxToBeAdded))
            print(self.jobIdxToBeAdded, self.jobs[self.jobIdxToBeAdded], "added!")
            self.jobIdxToBeAdded += 1

   def executeJob(self):
        if self.pq:
            duration, requestTime, idx = heappop(self.pq)
            self.time += duration
            self.sum += self.time - requestTime
            print("sum is", self.sum)
            self.completedJobs += 1
            print(duration, idx, "completed!")
            return True
        return False

    def computeAvg(self):
        return self.sum // self.completedJobs


# #############################################################################
# #############################################################################
# ############################## TEMPLATE AREA ################################
# #############################################################################
# #############################################################################

enu = enumerate


def argmax(arr):
    return max(enumerate(arr), key=lambda x: x[1])


def argmin(arr):
    return min(enumerate(arr), key=lambda x: x[1])


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


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()

