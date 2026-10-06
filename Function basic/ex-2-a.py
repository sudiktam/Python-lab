def get_product_remainder(num_1, num_2):
    product = num_1 * num_2

    if num_2 == 0:
        remainder = 'cannot divide by zero'

    else :
        remainder = num_1 % num_2

    return product, remainder

print(get_product_remainder(10, 3))
print(get_product_remainder(10, 0))