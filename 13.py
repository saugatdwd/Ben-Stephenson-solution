#Write a program to calculate total amount after n years if a person deposits p amount in a bank account yielding r percentage interest per year with
#interest compounded annually. [Hint: a = p × (1 + r / 100)n]

t=float(input("write time in year:"))
p=float(input("Write the amount that is deposited:"))
r=float(input("Write rate of interest:"))

a=p*(1+r/100)*r

print("The total amount after given time and rate is:",a)
