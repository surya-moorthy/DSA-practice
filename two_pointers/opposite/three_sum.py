def threeSum(nums):
    l = 0
    r = len(nums) - 1

    lst = []

    nums = sorted(nums)

    while(l < r):
        if(r - l - 1 >= 1):
            for k in range(l + 1, r):
                if(nums[l] + nums[r] + nums[k] == 0):
                    if(nums[l] != nums[r] and nums[r] != nums[k] and nums[l] != nums[k]):
                        lst.append(list((nums[l], nums[k] , nums[r])))
        
        if(abs(l) >= abs(r)):
            l += 1
        else:
            r -= 1
    
    print(lst)

lst = list(map(int , input("Enter the list : ").split(",")))

threeSum(lst)
