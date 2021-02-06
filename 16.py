#Write a program to input any 4 digit number and find the sum of first and last digit

a=int(input("Enter any 4 digit number:"))

sum=0

ld=a%10

fd=a

while a>=10:
    a=(a/10)

fd=a

sum=fd+ld

print("Sum of first digit and last digit is:",int(sum))
