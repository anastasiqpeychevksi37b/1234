n=int(input("Enter a number"))
a1=0
print("Fib:", a1, end=" ")
for i in range (1,10):
    a3 = a1 + n
    a1 = n
    n = a3
    print(a3, end=" ")
