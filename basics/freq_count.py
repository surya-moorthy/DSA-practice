input_str = input("Enter the string :")

freq = {}

for ch in input_str.replace(" ", ""):
        freq[ch] = freq.get(ch, 0) + 1
    
# for i in range(len(input_str)):
    
#     if(input_str[i] == ' '):
#         continue

#     if(input_str[i] in freq):
#         freq[input_str[i]] += 1
#     else:
#         freq[input_str[i]] = 1

print(freq)
