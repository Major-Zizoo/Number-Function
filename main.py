def add(x,y):
    return x+y

def sub(x,y):
    return x-y

print("1.add 2.sub")
choice=int(input("Enter 1 or 2:"))

x=int(input("Enter number:"))
y=int(input("Enter number:"))

if choice ==1:
    print(add(x,y))
elif choice ==2:
    print(sub(x,y))
else:
    print("Enter 1 or 2")