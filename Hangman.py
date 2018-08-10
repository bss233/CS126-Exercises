import random


def word_pick():
    """ Picks a word from the given list to use for the game of Hangman """
    word_list = ['apple', 'banana', 'cranberry', 'dragonfruit', 'grapefruit',
                 'kiwi', 'lemon', 'melon', 'nectarine', 'orange', 'pineapple',
                 'raspberry', 'tangerine', 'watermelon']
    answer = word_list[random.randint(0, 13)]
    return answer


def take_a_guess():
    """ Takes input in the form of a single character from the user to use as
    a guess.  """
    guess = input('Enter a letter: ')
    while len(guess) != 1:
        guess = input('Enter a letter: ')
    return guess


def find_number_of_occurences(word, letter):
    list_word = list(word)
    locations = []
    while letter in list_word:
        index = list_word.index(letter)
        locations.append(index)
        list_word.insert(index, '*')
        list_word.remove(letter)
    print('locations :' + str(locations))
    return locations


def update_word(guess, word, indexes):
    list_word = list(word)
    list_length = len(indexes)
    for i in range(list_length):
        position = indexes[i]
        list_word[position] = guess
    updated_word = ''.join(list_word)
    print('Updated Word: ' + updated_word)
    return updated_word


def main():
    answer = word_pick()
    strikes = 0
    guessed_letters = ''
    letters_to_guess = ''
    word_length = len(answer)
    for i in range(word_length):
        letters_to_guess += ' _ '
    completed_word = letters_to_guess
    print('Your word is: ' + completed_word)
    while completed_word != answer:
        if strikes < 6:
            current_guess = take_a_guess()
            guessed_letters += (' ' + current_guess)
            if current_guess in answer:
                locations = find_number_of_occurences(answer, current_guess)
                completed_word = update_word(current_guess, completed_word,
                                             locations)
            else:
                strikes += 1
            print(str((6 - strikes)) + ' Strikes remaining!')
            print(' ' + completed_word + ' ')
            print('Guessed letters: ' + guessed_letters)
    print('Game Over!')


if __name__ == "__main__":
    main()
