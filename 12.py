#Write a program to express a length given in millimeters in meters, centimeters, and millimeters.[Hint: 1 meter = 100 centimeter and 1 centimeter = 10 millimeter]

m=float(input("Write a  length in millimeters:"))

c=m/10
M=c/100

print("Length in centimeter is:",c)
print("Length in meters is:",M)
