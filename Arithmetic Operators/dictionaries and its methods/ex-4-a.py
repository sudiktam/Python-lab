student_info = {"name": "Ram", "age": 22, "grade": "A"}
student_info2 = student_info.copy()
student_info2['name'] = 'bob'
student_info2['grade'] = "B"
student_info2 = student_info
student_info2['age']= 30
print(student_info2)
print(student_info['name'])
print(student_info2['age'])
print(student_info2)
print(student_info)