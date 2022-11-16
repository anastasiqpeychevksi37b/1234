x=int(input("Write a number: "))
con=()
conn=()
a=str(x)
for item in a:
    print(item)
    con+=(item,)
for item in a[::-1]:
    print (item)
    conn+=(item,)
print(con)
print(conn)
