def get_count_vowels(string):
    string = string.lower()
    total_vowels = string.count("a") + string.count("e")  + string.count("i")  + string.count("o")  + string.count("u") 
    return total_vowels

name = input("Enter a name: ")
print(get_count_vowels(name))