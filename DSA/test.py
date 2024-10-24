import re


s = "0P"
cleaned_phrase = re.sub(r'[^a-zA-Z]', '', s).lower()
print(cleaned_phrase)