from codecs import open
from json import load

with open('txt_for_7.json', encoding='utf-8') as file:
    result = load(file)

print(result)
