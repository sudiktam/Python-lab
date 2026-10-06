my_num = [1,4,7,8,12,18]
# filter_num = lambda x : x % 3 == 0 
# result = list(filter(filter_num, my_num))
# print(result)
result = list(filter(lambda x : x % 3 == 0 ,my_num))
print(result )
