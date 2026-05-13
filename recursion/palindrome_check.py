string = input("Enter the input : ")

def palindrome(string):
    if string == "":
        return True
    
    n = len(string)

    if(string[0] != string[n  - 1]):
        return False

    return palindrome(string[1 : n - 1])

print(palindrome(string))