input_str = input("Enter the string : ")

new_str = ""

for i in range(len(input_str)):
    ch = input_str[i]
    
    if ch in "aeiou":
        new_str += '*'
    else:
        new_str += ch

print("After replacing vowels :", new_str)