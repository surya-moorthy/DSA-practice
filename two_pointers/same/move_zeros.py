def removeZeros(nums):
    slow = 0

    for fast in range(len(nums)):
        if(nums[fast] != 0):
            nums[fast] , nums[slow] = nums[slow], nums[fast]
            slow += 1
    
    print(nums)

lst = list(map(int , input("Enter the list : ").split(" ")))

removeZeros(lst)