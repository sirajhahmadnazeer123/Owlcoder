import sys
import time
start_time = time.time()
def coin_change(k, arr, dp):
    if k == 0:
        return 0
    if dp[k] != -1:
        return dp[k]
    
    ans = sys.maxsize
    for i in range(len(arr)):
        if arr[i] <= k:
            ans = min(ans, 1 + coin_change(k - arr[i], arr, dp))
    
    dp[k] = ans
    return dp[k]

n = int(input())
s = list(map(int, input().split()))
s.sort()
dp = [-1] * (n + 1)
result = coin_change(n, s, dp)
print(result)
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
