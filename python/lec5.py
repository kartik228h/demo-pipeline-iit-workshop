i=int(input("enter the number"))
x=2
while x<=i-1:
    if i%x==0:
        break
    x+=1
if x==i:
    print("prime")
else:
    print("not prime")       