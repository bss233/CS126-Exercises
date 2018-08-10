import random


def word_pick():
    """ Picks a word from the given list to use for the game of Hangman """
    word_list = ['apple', 'banana', 'cranberry', 'dragonfruit', 'grapefruit',
                 'kiwi', 'lemon', 'melon', 'nectarine', 'orange', 'pineapple',
                 'raspberry', 'tangerine', 'watermelon']
    # answer = word_list[random.randint(0, 13)]
    return word_list[0]


def take_a_guess():
    """ Takes input in the form of a single character from the user to use as
    a guess.  """
    guess = input('Enter a letter: ')
    while len(guess) != 1:
        guess = input('Enter a letter: ')
    return guess


def find_number_of_occurences(word, letter):
    list_word = create_list_word(word)
    locations = []
    while letter in list_word:
        index = list_word.index(letter)
        locations.append(index)
        list_word.insert(index, '*')
        list_word.remove(letter)
    return locations


def create_list_word(word):
    list_word = []
    word_length = len(word)
    for i in range(word_length):
        list_word.append(' _')
    return list_word


def update_word(guess, word, indexes):
    list_word = create_list_word(word)
    list_length = len(indexes)
    for i in range(list_length):
        position = indexes[i]
        list_word[position] = guess
    return list_word


def status(word, strikes, letters):
        print(str((6 - strikes)) + ' Strikes remaining!')
        print(' ' + word + ' ')
        print('Guessed letters: ' + letters)


def main():
    answer = word_pick()
    list_word = create_list_word(answer)
    strikes = 0
    guessed_letters = ''
    string_word = ''.join(list_word)
    status(string_word, strikes, guessed_letters)
    while string_word != answer:
        if strikes < 6:
            current_guess = take_a_guess()
            guessed_letters += (' ' + current_guess)
            if current_guess in answer:
                locations = find_number_of_occurences(answer, current_guess)
                temp_word = update_word(current_guess, string_word,
                                        locations)
                string_word = ''.join(temp_word)
            else:
                strikes += 1
            status(string_word, strikes, guessed_letters)
    print('Game Over!')


if __name__ == "__main__":
    main()
