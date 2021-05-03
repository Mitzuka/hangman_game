from random import randint


def select_word() -> str:

    with open('./data.txt', 'r', encoding='utf-8') as f:
        word = f.readlines()

    return word[randint(1,len(word))]


def normalize(word) -> str:

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


def game():
    pass


def run():
    print(normalize(select_word()))


if __name__ == '__main__':
    run()