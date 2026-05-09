string = input("Enter the string : ")

lst = []

brack_list = list(string)

for brac in brack_list:

    if(brac == '{' or brac == '[' or brac == '('):
        lst.append(brac)
        brack_list.remove(brac)
    else:
        if((brac == '}') == (lst[len(lst) - 1] == '{') or (brac == ')') == (lst[len(lst) - 1] == '(') or (brac == ']') == (lst[len(lst) - 1] == '[')):
            brack_list.remove(brac)

if(len(lst) > 0 or len(brack_list) > 0):
    print("false")
else:
    print("true")