x=int(input("Enter a num"))
a=[i for i in range (0,x)]
print(a)
dictionary={}
for index in range(len(a)):
    dictonary[index]=a[-1-index]
print(dictionary)
