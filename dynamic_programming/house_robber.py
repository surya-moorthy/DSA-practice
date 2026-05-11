lst = list(map(int , input("Enter the list : ").split(" ")))

dp = [0] * (len(lst))

n = len(lst)

if n == 0:
    print(0)

elif n == 1:
    print(lst[0])

else:
    for i in range(len(lst)):
        if i == 0:
            dp[0] = lst[0]
        elif i == 1:
            dp[1] = max(lst[0],dp[1])
        else:
            dp[i] = max(dp[i - 1], dp[i - 2] + lst[i])

print(dp)

print(dp[n - 1])