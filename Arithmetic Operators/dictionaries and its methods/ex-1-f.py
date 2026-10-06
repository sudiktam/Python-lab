student_info = {"name": "Ram", "age": 22, "grade": "A", "courses": ["DS", "SQL"]}
address = student_info.get("address")
address = student_info.get("address", "Address not found")
print(address)