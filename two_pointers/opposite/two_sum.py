size = int(input("Enter the size : "))

lst = []

print("Enter the elements : ")
for i in range(size):
    lst.append(int(input()))

target = int(input("Enter the target Sum : "))

found = 0

l = 0
r = size - 1

while(l < r):
   
    sum = lst[l] + lst[r]
   
    if(sum < target):
        l += 1
    elif(sum > target):
        r -= 1
    else:
        print(f"The values that get target sum {target} : {lst[l], lst[r]}")
        found = 1
        break

if(found == 0):
    print("Can't able to find the two numbers that get the target sum")

