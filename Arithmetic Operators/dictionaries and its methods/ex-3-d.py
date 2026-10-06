student_info = {"name": "Ram", "age": 22, "grade": "A", "courses": ["DS", "SQL"]}
address = student_info.get('address')
address = student_info.get('address','address not found')
grade = student_info.get('grade')
print(grade)
print(address)
