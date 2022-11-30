n=int(input("Enter a number"))
sum=0
b=n
for i in range (0,n):
    print(b)
    sum=sum+b
    b=b*10+n
print("\n c:",sum)
