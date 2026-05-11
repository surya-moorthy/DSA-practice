def threeSum(nums):
    l = 0
    r = len(nums) - 1

    lst = []

    nums = sorted(nums)

    n = len(nums)

    for i in range(n - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        j , k = i + 1, n - 1

        while(j < k):
            sum = nums[i] + nums[j] + nums[k]

            if(sum > 0):
                k -= 1
            elif(sum < 0):
                j += 1
            else:
                lst.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1

            while(nums[j] == nums[j - 1]):
                j += 1

            while(nums[k] == nums[k + 1]):
                k -= 1
    
    print(lst)

lst = list(map(int , input("Enter the list : ").split(",")))

threeSum(lst)
