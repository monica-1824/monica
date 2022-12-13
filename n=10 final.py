n=10
n1=int(input("enter the number"))
n2=int(input("enter the number"))
print(n1),print(n2)
for i in range(0,10):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
