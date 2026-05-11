n = int(input("Enter the input : "))

a , b , c = 0 , 1 , 1

for i in range(n - 2):
    d = a + b + c
    a , b , c = b , c , d

print(c)