lst = list(map(int , input("Enter the list").split(",")))

def sum_of_lst(lst, length, sum):
    if(length == len(lst)):
        return sum
    
    return sum_of_lst(lst, length + 1, sum + lst[length])

print(sum_of_lst(lst, 0, 0))