num = int(input("Enter the number : "))
changes = [2,3,5]

# state : min coins to make num == k
#  transition : dp[i] = min(dp[k - coin of coins])

min_count = [float('inf')]

def min_coin_change_recursive_way(changes, num, count):
    if num == 0:
        min_count[0] = min(min_count[0], count)
        return
    
    for change in changes:
        if num >= change:
            min_coin_change_recursive_way(changes, num - change, count + 1)
        else:
            break

def dp_approach(changes, num):
    dp = [float('inf')] * (num + 1)

    dp[0] = 0

    changes.sort()

    for i in range(1, num + 1):
        for change in changes:
            if i >= change:
                dp[i] = min(dp[i], dp[i - change] + 1)
            else:
                break

    print(dp[num] if dp[num] != float('inf') else -1)
