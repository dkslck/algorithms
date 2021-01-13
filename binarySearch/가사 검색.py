# time complexity: O(NlogN + M*MlogM)
def solution(words, queries): # N = len(words) # M = len(queries)
    from bisect import bisect_left, bisect_right
    prefix = [(len(x), x) for x in words] # O(N)
    prefix.sort() # O(NlogN)
    postfix = [(len(x), x[::-1]) for x in words] # O(NlogN)
    postfix.sort()
    ans = []
    for query in queries: # O(M * MlogM)
        ln = len(query)
        q = (ln, query)
        usedArray = prefix
        if query[0] == '?' or query[-1] == '?':
            queryPre = query.replace('?', 'a')
            queryPost = query.replace('?', 'z')
            if query[0] == '?':
                qPre = (ln, queryPre[::-1])
                qPost = (ln, queryPost[::-1])
                usedArray = postfix
            else:
                qPre = (ln, queryPre)
                qPost = (ln, queryPost)
        else:
            qPre, qPost = q, q
        iB = bisect_left(usedArray, qPre) # O(MlogM)
        iE = bisect_right(usedArray, qPost) # O(MlogM)
        ans.append(iE - iB)

    return ans
