name = input("enter your name :")
age = int(input("enter your age :"))
salary = int(input("enter your salary :"))

if age >= 25 and age <= 50 and salary >= 50000:
    print(f"{name}, you are eligible for the loan")

else : 
    print (f"{name}, you are not eligible for the loan")
