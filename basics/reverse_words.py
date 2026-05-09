def str_reverse(string):

    str_rev = ""
    r = len(string) - 1
    
    while(r >= 0):
        str_rev += string[r]
        r -= 1

    return str_rev


string = input("Enter the sentence : ")

str_rev = str_reverse(string)
print("reverse string : ",str_rev)

str_split = list(str_rev)

l = 0

result = ""

for i in range(len(str_split)):
    
    if(i == len(str_split) - 1 or str_split[i + 1] == ' '):
        r = i
        
        while(r > l):
            
            temp = str_split[r]
            str_split[r] = str_split[l]
            str_split[l] = temp

            r -= 1
            l += 1
        
        l = i + 2

        print(str_split)

print("".join(str_split))



