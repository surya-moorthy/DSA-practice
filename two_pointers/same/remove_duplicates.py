def removeDuplcicates(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
    
    for i in range(slow + 1, len(nums)):
        nums[i] = '_'

    print(f"final list : {nums}")
    
    return slow + 1

lst = list(map(int , input("Enter the list : ").split(" ")))

result_length = removeDuplcicates(lst)

print("Result length : ", result_length)