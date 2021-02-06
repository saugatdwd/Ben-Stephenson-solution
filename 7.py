#Write a program to find area and circumference of circle. Use PI as a symbolic constant. [Hint: area = r2; circumference = 2r]

r=float(input("Enter radius of a circle:"))
PI=22/7

area=PI*r*r
circumference=2*PI*r

print("Area of circle is:",area)
print("Circumference of circle is:",circumference)
