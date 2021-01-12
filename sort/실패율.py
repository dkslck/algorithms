
# algorithm used: sort
# data structure: python list
# time complexity: O(N * logM + M * logM + N * logN) == O((N+M) * logM + N * logN) 
def solution(N, stages):
    M = len(stages)
    freq =  [0] * N
    for i in stages: # frequency calculation: O(M)
        if i == N+1: continue # to avoid array index out of bound
        freq[i-1] += 1
    stages.sort() # O(MlogM)
    from bisect import bisect_left as bi
    reached = [M - bi(stages, i+1) for i in range(N)] # O(N * logM)
    reached = [i if i != 0 else 1 for i in reached] # get rid of zeros to avoid division by zero error
    
    frac = [i/j for i, j in zip(freq, reached)] # O(N)
    forSort = [(-e, i) for i, e in enumerate(frac)] # O(N)
    forSort.sort() # O(NlogN)
    ans = [i[1]+1 for i in forSort] #O(N)
    return ans
