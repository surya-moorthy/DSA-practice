x = int(input("Enter the number : "))
n = int(input("Enter the power : "))

def power(x,n):
    if n == 0:
        return 1
    
    if n == 1:
        return x
    
    half = power(x,n//2)

    if n % 2 == 0:
        return half * half
    else:
        return half * half * power(x,n%2)

print(power(x,n))