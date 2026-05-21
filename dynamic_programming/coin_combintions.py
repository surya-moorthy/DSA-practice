# state : number of ways to form i
# transition : dp[i] = dp[i - coin of coins]

def coin_combinations(coins, num):
    dp = [0] * ( num + 1)
    dp[0] = 1

    for i in range(1, num + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] += dp[i - coin]
    
    print(dp[num])


coin_combinations([2,3,5],11)