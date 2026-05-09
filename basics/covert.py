input_str = input("Enter the string : ")

result_str = ""

for i in range(len(input_str)):

    if(i == 0 or input_str[i - 1] == ' '):
        result_str += input_str[i].upper()
    else:
        result_str += input_str[i]

print("Result string as title : ", result_str)