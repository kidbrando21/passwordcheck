import re

print("A good password has 12 or more characters, upper and lower case letters, numbers, and symbols Also No words in the english dictionary")

password = input("insert pass here: ")

desired_length = 12

length = len(password)

def check_string(password, wordlist_filename):
    has_letters = bool(re.search(r'[a-zA-Z]', password))
    has_lowletters = bool(re.search(r'[a-z]', password))
    has_numbers = bool(re.search(r'\d', password))
    has_symbols = bool(re.search(r'[^a-zA-Z0-9\s]', password))

    with open(wordlist_filename, "r") as wordlist_file:
        wordlist = wordlist_file.read().splitlines()

    if has_letters and has_numbers and has_lowletters and has_symbols and length >= desired_length:
        contains_words = False
        for word in wordlist:
            if word.lower() in password.lower():
                contains_words = True
                break

        if contains_words:
            return "Password is not strong enough."
        else:
            return "Strong password."
    else:
        return "Password does not meet the criteria."

results = check_string(password, "words.txt")
print(results)

