import re

with open('words.txt', 'r') as wordlist_file:
    original_wordlist = wordlist_file.read().splitlines()


filtered_wordlist = [word for word in original_wordlist if re.match(r'^[a-zA-Z]{3,}+$', word)]

with open('words.txt', 'w') as wordlist_file:
     wordlist_file.write('\n'.join(filtered_wordlist))
     
