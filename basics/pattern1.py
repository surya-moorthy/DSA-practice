n = int(input("Enter the number : "))

for i in range(n):
    num = 1
    for j in range(n):
        if(j >= n - i - 1) : 
            print(num, end='')
            num += 1
        else:
            print(' ', end='')
        
    print()