import random
word_list = ['apple', 'banana', 'coconut', 'dragonfruit', 'grapefruit', 'kiwi',
            'lemon', 'melon', 'nectarine', 'orange', 'pineapple', 'raspberry',
            'tangerine', 'watermelon']
strikes = 0
answer = word_list[random.randint(0, 13)]
for letter in answer:
    print('')


def take_a_guess():
    guess = input('Enter a letter: ')
    while len(guess) != 1:
        guess = input('Enter a letter: ')
    return guess
