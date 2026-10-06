name = input("enter your name :")
birth_year = int(input( "enter your age :"))

current_year = 2026
age = current_year - birth_year
if age >= 18:
    print(f"{name}, you are eligible for voting")