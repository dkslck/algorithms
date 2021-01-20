def solution(stones, k):
    count = 0
    # transfer maximum number of people while satisfying k == lowerboundK(stones, val)
    return binRight(k, min(stones), max(stones)+1, stones) - 1


# Returns the rightmost index where 'val' can fit in a sorted list.
# e.g. 1 1 1 2 2 2 3 3 5 5 <- binRight(2) returns 6
def binRight(val, left, right, stones):
    if left == right:
        return left
    mid = (left + right) // 2
    midVal = lowerboundK(stones, mid)
        
    if val < midVal:
        return binRight(val, left, mid, stones)
    else:
        return binRight(val, mid+1, right, stones)


# minimum number of k required for 'people' people to cross the river.
def lowerboundK(stones, people):
    people -= 1
    stones = [stone - people for stone in stones]
    maxCount = 0
    count = 0
    for stone in stones:
        if stone <= 0:
            count += 1
            maxCount = max(maxCount, count)
        else:
            count = 0
    return maxCount+1
