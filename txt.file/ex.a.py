file_path = r'loop.txt'
content = ['I am learning Python programming.', 'It is a versatile language.', 'I enjoy solving problems with code.']

with open(file_path, 'w', encoding='utf-8') as file_obj:
    file_obj.writelines('\n'.join(content))

new_content = 'I am learning Python programming.\nIt is a versatile language.'
with open(file_path, 'w', encoding='utf-8') as file_obj:
    file_obj.write(new_content)
