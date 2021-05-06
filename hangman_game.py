from random import randint
from os import system


def select_word() -> str:
    '''Return word from a data file'''
    with open('./data.txt', 'r', encoding='utf-8') as f:
        word = f.readlines()

    return word[randint(1,len(word))]


def normalize(word) -> str:
    '''Replace the vocals with accents'''

    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        word = word.replace(a, b)
    
    return word


def clear_screen():
    if system('clear') == 1:
        system('cls')


def hide_word(word) -> dict:
    '''Return "_" in a dict'''
    blank_space = {i:' _ ' for i in range(len(word))}
    blank_space.popitem()
    return blank_space


def answer_dict(word) -> dict:
    answer = dict(enumerate(word))
    answer.popitem()
    return answer
    

def find_letter(word, letter) -> list:
    '''It saves the location number of the letter'''
    list_numbers = []
    count = 0

    for i in word:
        if i == letter:
            list_numbers.append(count)
        count += 1
    return list_numbers


def fill_space(word, blank_space, list_numbers) -> dict:
    blank_dict = blank_space

    for i in list_numbers:
        blank_dict[i] = word[i]

    return blank_dict


def blank_word(blank_space) -> str:
    spaces = ''

    for i in blank_space.values():
        spaces += i
    
    return spaces



def game():

    # Config
    word = normalize(select_word()) 
    blank_space = hide_word(word)
    space = ''
    letter = ''
    answer = blank_word(answer_dict(word))

    # Loop-Game
    while True:

        clear_screen()
        space = blank_word(blank_space)

        if space == answer:
            print('Congrats. You Won.')
            break
        
        else:
            print(space)
            
            letter = input('\nIngresa una letra -> ')

            place_letter = find_letter(word, letter)
            blank_space = fill_space(word, blank_space, place_letter)


    print(f'Word: {answer}')

def run():
    game()

if __name__ == '__main__':
    run()