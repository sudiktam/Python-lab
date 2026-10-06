def is_palindrome(string):
    reverse = string[::-1]
    if string == reverse:
        return True 

    else: 
        return False

print(is_palindrome("racecar"))  