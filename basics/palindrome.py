input_str = input("Enter the string : ")

found = 1

l = 0
r = len(input_str) - 1

while(l < r):
    if(input_str[l] != input_str[r]):
        found = 0
        break
    else:
        l += 1
        r -= 1
        
if found: print("given string is palindrome")
else : print("given string is not palindrome")