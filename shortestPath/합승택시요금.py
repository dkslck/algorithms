def solution(n, s, a, b, fares):
    s -= 1
    a -= 1
    b -= 1

    mat = [[10**9 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        mat[i][i] = 0

    for from_, to, fare in fares:
        from_ -= 1
        to -= 1
        mat[from_][to] = fare
        mat[to][from_] = fare

    for k in range(n):
        for i in range(n):
            for j in range(n):
                val = mat[i][k] + mat[k][j]
                if mat[i][j] > val:
                    mat[i][j] = val

    sum_ = 10 ** 9
    for i in range(n):
        val = mat[s][i] + mat[i][a] +mat[i][b]
        if sum_ > val:
            sum_ = val

    return sum_
