def solution(n):
    count = 1
    inc = 1
    while n > inc:
        n -= inc
        inc += 1
        q, r = divmod(n, inc)
        if r == 0:
            print(q, r, count)
            count += 1
    return count
