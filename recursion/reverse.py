string = input("Enter the string : ")

def reverse_string(str):
    if str == "":
        return str
    
    return reverse_string(str[1:]) + str[0]
print(reverse_string(string))