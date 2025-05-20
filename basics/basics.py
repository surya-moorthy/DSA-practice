def hello() :
    enter_type = input("enter the datatype to create:")
    if enter_type == "int":
        int_type = int(input("Enter your integer:"))
        print("the number is: ",int_type)
    elif enter_type == "str":
        strType = input("Enter your string:")
        print("the number is: ",strType)
    elif enter_type == "float":
        floatType = input("Enter your float:")
        print("the float number is:",float(floatType))
    elif enter_type == "bool":
        print("the bool value:",True)
    elif enter_type == "list":
        listType = list(input("Enter your list:"))
        print("the list is:",listType)
    elif enter_type == "tuple":
        tupleType = tuple(input("Enter your tuple:"))
        print("the float number is:",float(tupleType))
    elif enter_type == "set":
        floatType = set(input("Enter your float:"))
        print("the float number is:",float(floatType))
    elif enter_type == "dict":
        d = {}
        key = input("Enter your key:")
        value = input("Enter your value")
        d[key] = value
        print("the dict value is:",d)
    else:
        print("Invalid type")

if __name__ == "__main__":
    while True:
        start = input("do you wanna start? (y/n)")
        if start == "y":
            hello()
        elif start == "n":
            exit()