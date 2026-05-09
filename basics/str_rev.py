input_str = input("Enter the string : ")

input_list = list(input_str)

l = 0
r = len(input_str) - 1

while(l < r):
    input_list[l], input_list[r] = input_list[r] , input_list[l]
    l += 1
    r -= 1

input_str = "".join(input_list)

print("Reversed String :", input_str)