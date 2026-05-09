input_str = input("Enter the string : ")

freq = [0]*26

new_str = ""

for ch in input_str.lower():
    if(freq[ord(ch) - ord('a')] == 0):
        new_str += ch
        freq[ord(ch) - ord('a')] = 1

print("After duplicates :",new_str)