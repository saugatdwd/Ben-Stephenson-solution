#Write a program to sum the digits of a positive integer which is 5 digits long.

a=int(input("Enter 5 digit long integer:"))

sum=sum(int(digit) for digit in str(a))

print("Sum of the digits is:",sum)
