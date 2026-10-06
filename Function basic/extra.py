# def get_simple_interest(principal, rate, time):
#     simple_interest = (principal * rate * time)/100
#     return simple_interest

# interest = get_simple_interest(100,10,5)
# print(int(interest)) 

# def get_rectangle_area_perimeter(length, width):
#     area = (length * width)
#     perimeter = 2 *(length + width)
#     return area, perimeter

# total_area = get_rectangle_area_perimeter(5,10)
# print(total_area)


# def is_palindrome(string):
#     word = string[::-1]
#     if string== word:
#         return "Ture "
    
#     else:
#         return"False"

# print(is_palindrome("madam"))


# country_list = ["india", "uSA", "uK", "canada", "australia"]
# country_dict = dict()

# for country in country_list:
#     key = country[0].upper()
#     value = country.title()
#     country_dict[key] = value

# print(country_dict)

# From_marks_list = [20,30,50,80,90,10,60,5]
# passed_marks = []
# Failed_marks = []

# for mark in From_marks_list:
#     if mark < 32:
#         Failed_marks.append(mark)
#     else:
#         passed_marks.append(mark)

# print("Passed marks:", passed_marks)
# print("Failed marks:", Failed_marks)


def count_p(user_string):
    count = 0
    for p in user_string:
        if p == 'p':
            count += 1
    return count

name = "apple"
count_of_p = count_p(name)
print(count_of_p)


      
