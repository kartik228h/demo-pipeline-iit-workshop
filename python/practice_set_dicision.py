x=int(input("enter the length of the rectangle"))
y=int(input("enter the breadth of the rectangle"))
z=x*y
print("the area of a rectangle is",z)

p=int(input("enter the principle amount:"))
r=float(input("entr the rate of interest:"))
t=int(input("enter the time:"))
simple_interest=(p*r*t)/100
print("simple interest is",simple_interest)

#to remove last digit from a number
x=int(input("enter the number:"))
z=x%10
print("last diget of the number is",z)

#to swap data of two numbers 
x=int(input("enter the number:"))
y=int(input("enter the number:"))
z=x
x=y
y=z
print("after swapping value of x and y are",x,y)

#divisible by 5 or not
x=int(input("enter the number"))
if x%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")   

#to print two given words in dictionary order
x=input("enter the word 1:")
y=input("enter the word 2:")
if x<y:
    print(x,y)
else:
    print(y,x)    

#to check wheather a given number is three digit or not
x=int(input("enter the number"))
if (100<=x<=999 or -100<=x<=-999 ):
    print("given number is a three digit number")
else:
    print("given number is not a three digit  number ")     

#to cheak wheather a year is leap year or not
x=int(input("enter the year:"))
if  (x%400==0) or (x%4==0 and x%100!=0) :
    print(f"{x}is a leap year")
else:
    print(f"{x}is not a leap year")   

#to check wheather a given number is positive negative or zera
x=int(input("enter the number"))

if x>0:
    print(f"{x} is a positive number")
elif x<0:
    print(f"{x} is a negative number ")    
else:
    print(f"{x} is zero")    

#accept a complex number from user and tell which is greater real or imagenary part
x=complex(input("enter the complex number"))
real_num=x.real
imag_num=x.imag

if real_num>imag_num:
    print(f"{real_num} is greater")
else:
    print(f"{imag_num} is greater")    


