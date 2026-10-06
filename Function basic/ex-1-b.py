def get_rectangle_area(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

result  = get_rectangle_area(5, 3)
print (result)