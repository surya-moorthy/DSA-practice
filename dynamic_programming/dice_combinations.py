def diceCombination( n):
    dp = [0] * (n + 1)

    dp[0] = 1

    for i in range(1,n + 1):
        for face in range(1, 7):
            if i - face >= 0:
                dp[i] += dp[i - face]
        
    print(dp[n])

diceCombination(7)
        
