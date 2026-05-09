n = int(input("Enter the number : "))

for i in range(n):
    
    if(i < (n - 1)/2):
        left = (n - 1)/2 - i
        right = (n - 1)/2 + i 
    else:
        left = (n - 1)/2 - (n - i) + 1
        right = (n - 1)/2 + (n - i) - 1

    for j in range(n):
        if(j >= left and j <= right):
            print("*", end='')
        else:
            print(' ', end='')
    print()
