str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

stat = "Not anagram"

cond = 1

if len(str1) != len(str2):
    cond = 0

else:
    
    freq = {}

    for ch in str1:
        dict[ch] = dict.get(ch, 0) + 1

    for ch in str2:
        present = dict.get(ch , 0)

        if(present > 0):
            dict[ch] = dict.get(ch, 0) - 1
        else:
            cond = 0
            break

if(cond):
    print("both are anagram")
else:
    print(stat)