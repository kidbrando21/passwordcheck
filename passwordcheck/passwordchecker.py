import re

password = input("inset pass here ")

desired_length = 7

length = len(password)

def check_string(password):
    has_letters = (re.search(r'[a-zA-z]', password))
    has_numbers = (re.search(r'\d', password))
    has_symbols = (re.search(r'[^a-zA-Z0-9\s]', password))
    
    if has_letters and has_numbers and has_symbols and length >= desired_length:
        return ("you have a strong password")
    else:
        return ("the password is not strong enough")

results = check_string(password)

print(results)

