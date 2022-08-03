import requests
import json


def get_word(word: str):
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    word = json.loads(response.text)

    try:
        return word[0]['word']
    except KeyError:
        return 'not a word'


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in alphabet:
    temp_word = input(str(f'{letter}: '))
    while temp_word[0].lower() != letter:  
        print(f"word {temp_word} doesn't start with {letter}")
        temp_word = input(str(f'{letter}: '))

    _ = get_word(temp_word)
    while _ == 'not a word':
        print("word doesn't exist")
        temp_word = input(str(f'{letter}: '))
        _ = get_word(temp_word)
