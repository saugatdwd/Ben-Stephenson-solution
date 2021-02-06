#Write a program to print a six digit integer in reverse order.

a=int(input("Enter six digit integers:"))

b=0

while(a>0):
    remainder=a%10
    b=(b*10)+remainder
    a=a//10

print("The given six digit integer in reverse order is:{}".format(b))
