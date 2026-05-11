n = int(input("Enter the number : "))

dp = [n] * (n + 1)
dp[0] = 0

for target in range(1,n + 1):
    for sq in range(1,target + 1):
        square = sq * sq

        if target - square < 0:
            break

        dp[target] = min(dp[target], dp[target - square] + 1)

print(dp[n])