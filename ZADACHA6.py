text=str(input("write a text"))
dictionary={}
print(text)
for item in text:
    print(item)
    if item in dictionary:
        dictionary[item]+=1
    else:
        dictionary[item]=1
print(dictionary)
