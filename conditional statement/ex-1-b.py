num_1 = int(input('enter num_1 :'))
num_2 = int(input('enter num-2 :'))

if num_2 == 0 :
    print('cannot divide by zero')

elif num_1 % num_2 == 0:
    print(f"{num_1} is divisible by {num_2}")
else:
    print(f"{num_1} is not divisible by {num_2}")