def get_vals(n, m, maps, dp):
    # base_case
    if n < 0 or m < 0:
        return 0
    if n == 0 and m == 0:
        return 1
    if dp[n][m] != -1:
        return dp[n][m]
    if maps[n][m] == 1:
        return 0
    left = get_vals(n, m - 1, maps, dp)
    up = get_vals(n - 1, m, maps, dp)
    dp[n][m] = left + up
    return dp[n][m]

n, m = map(int, input().split())
g = []
for i in range(n):
    l = list(map(int, input().split()))
    g.append(l)
mat = [[-1 for _ in range(m)] for _ in range(n)]
result = get_vals(n - 1, m - 1, g, mat)
print(result)
