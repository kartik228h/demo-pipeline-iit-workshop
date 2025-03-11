#to print first 10 odd natural nuymbers
'''x=0
while x<10:
    x=x+1
    if x%2!=0:
     print(x)

#to print even natural numbers
x=0
while x<10:
    x=x+1
    if x%2==0:
        print(x)

#to print first 10 odd natural numbers in reverse order
x=10
while x>0:
    x=x-1
    if x%2!=0:
        print(x)

#to print squares of first n natural numbers
x=1
y=int(input("enter the number"))
while x<=y:
 
    z=x**2
    print(z)
    x=x+1

#sum of first n natural numbers
x=0
n=int(input("enter the numbars:"))
sum=0
while x<=n:
    sum=sum+x
    x=x+1
print(sum)  

#to calculate factorial of a number
n = 5 
result = 1

for i in range(1, n + 1):
    result *= i

print(result)  

#to count digits in a given number
x=int(input("enter the number"))
count=0
while x>0:
    count=count+1
    x=x//10
print (count)   

#sum of the digits of the number
x=int(input("enter the number"))
sum=0
while x>0:
    sum=sum+x%10
    x=x//10
print (sum) ''

#a givemn number is a prime or not
n=int(input("enter the number"))
i=2
while i<=n-1:
    if n%i==0:
        break
    i=i+1  

if n==i:
    print("prime")
else:
    print("not prime")  '''


