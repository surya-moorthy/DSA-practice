n = int(input())

# state : subtract one of the digits to give minimal number of steps to reduce the number to 0
# transition : dp[i] = min(dp of each digits)

dp = [float('inf')] * (n + 1)

dp[0] = 0

for i in range(1,n + 1):
    temp = i

    while temp > 0:
        digit = temp % 10
        
        if digit != 0:
            dp[i] = min(dp[i],dp[i - digit] + 1) 

        temp = temp // 10

print(dp[n])