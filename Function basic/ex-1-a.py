def get_simple_interest(principal, rate, time ):
    simple_interest = (principal *rate *time )/100
    return simple_interest

interest = get_simple_interest(1000, 5, 2)
print(interest)