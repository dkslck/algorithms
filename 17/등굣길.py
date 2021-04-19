MOD = 1000000007

def DP(x, y):
    if dp[x][y] is not None:
        return dp[x][y]

    sum_ = 0
    if x != 0:
        up = DP(x-1, y)
        if up != -1:
            sum_ += up

    if y != 0:
        left = DP(x, y-1)
        if left != -1:
            sum_ += left

    dp[x][y] = sum_ % MOD
    return dp[x][y]




def solution(m, n, puddles):
    global dp
    dp = Mat(m, n)
    dp[0][0] = 1
    for i, j in puddles:
        dp[i-1][j-1] = -1
    return DP(m-1, n-1)

def Mat(h, w, default=None):
    return [[default for _ in range(w)] for _ in range(h)]
