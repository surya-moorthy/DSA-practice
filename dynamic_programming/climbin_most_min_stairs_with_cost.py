lst = list(map(int , input("Enter the list : ").split(" ")))

n = len(lst)

dp = [0] * (n + 1)

dp[0] = lst[0]
dp[1] = lst[1]


for i in range(2, n):
    dp[i] = lst[i] + min(dp[i - 1], dp[i - 2])

dp[n] = min(dp[n - 1],dp[n - 2])

print(dp[n])
