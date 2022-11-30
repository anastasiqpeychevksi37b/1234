number=int(input("Enter a number"))
f=1
if number < 0 :
    print ("does not have factorial")
elif number == 0 :
    print("1")
else:
    for i in range (1,number + 1):
        f = f*i
        print(number,"*",i,"=",f)
print(number,n)
