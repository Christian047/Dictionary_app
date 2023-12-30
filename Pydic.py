# import libraries    
from PyDictionary import PyDictionary


print('Welcome to Python Dictionary')

# Create an instance of the object
dictionary = PyDictionary()

# Create a repeated function
while True:
    word = input('Enter your word here: ')
    if word == '':
        break
    
    # Filter for ord meanings
    meanings = dictionary.meaning(word)
    
    # Loop through and present the word and definitions
    if meanings:
        print(f'Meanings of "{word}":')
        for part_of_speech, definition_list in meanings.items():
            print(f'{part_of_speech}:')
            for index, definition in enumerate(definition_list, start=1):
                print(f'  {index}. {definition}')
    else:
        print(f'Sorry, no meanings found for "{word}"')
