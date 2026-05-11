lst =  [[1,1],[2,2],[3,3],[4,4],[5,5]]

dp = [0] * (len(lst))

maxi = 0

for i in range(len(lst)):

    points , power = lst[i]
    dp[i] = dp[i] + points

    point = i + power + 1
    
    if point < len(lst):
        dp[point] = max(dp[i],dp[point])
    
    if( maxi < dp[i]):
        maxi = dp[i]

print(dp)

print(maxi)