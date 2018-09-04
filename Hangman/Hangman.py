import random


def word_pick():
    """ Picks a word from the given list to use for the game of Hangman """
    word_list = ['apple', 'banana', 'cranberry', 'dragonfruit', 'elderberry',
                 'fig', 'grapefruit', 'honeydew', 'jackfruit', 'kiwi', 'lemon',
                 'mango', 'nectarine', 'orange', 'pineapple', 'quince',
                 'raspberry', 'strawberry', 'tangerine', 'watermelon',
                 'zucchini']
    answer = word_list[random.randint(0, 13)]
    return answer


def take_a_guess():
    """ Takes input in the form of a single character from the user to use as
    a guess.  """
    guess = input('Enter a letter: ').lower()
    while len(guess) != 1:
        guess = input('Enter a letter: ')
    if not guess.isalpha():
        print('Please only enter letters')
        take_a_guess()
    return guess


def find_number_of_occurences(word, guess):
    """ Finds the number of times a character appears in a given word
    :param list word: The word to be checked
    :param character guess: The character to be searched for
    :return: Returns a list that contains the indices of each character in the
    given word
    """
    locations = []
    search_for = guess
    for index, letter in enumerate(word):
        if letter == search_for:
            locations.append(index)
    return locations


def create_blank(word):
    """ Creates a list that contains '_' equal to the number of characters in
    the given word
    :param word: A word in string form to be converted into a string of '_'s
    :return: Returns a list containing only '_'s equal to the number of
    characters in the given word
    """
    list_word = list(word)
    list_length = len(word)
    for i in range(list_length):
        list_word[i] = '_'
    return list_word


def update_word(letter, word, indexes):
    """ Takes in a word as a list to update with a given letter at given
    indexes
    :param letter: The letter to add as a character
    :param word: The word to update as a list
    :param indexes: The location of each letter as integers in a list
    :return: Returns a list that contains the updated word
    """
    list_length = len(indexes)
    for i in range(list_length):
        position = indexes[i]
        word[position] = letter
    return word


def status(word, strikes, letters):
    """
    :param word: List, The word that the user has guessed so far
    :param strikes: Int, The numbers of strikes the user has used so far
    :param letters: String, The letters the user has already guessed
    """
    spaced_word = ' '.join(word)
    print(str((6 - strikes)) + ' Strikes remaining!')
    print('Guessed letters: ' + letters)
    print(spaced_word)
    print('\n')


def main():
    answer = word_pick()
    working_word = create_blank(answer)
    strikes = 0
    guessed_letters = ''
    player_answer = ''
    status(working_word, strikes, guessed_letters)
    while player_answer != answer:
        if strikes < 6:
            current_guess = take_a_guess()
            guessed_letters += (current_guess + ' ')
            if current_guess in answer:
                locations = find_number_of_occurences(answer, current_guess)
                working_word = update_word(current_guess, working_word,
                                           locations)
            else:
                strikes += 1
            player_answer = ''.join(working_word)
            status(player_answer, strikes, guessed_letters)
        else:
            print('The word was: ' + answer)
            break
    print('Game Over!')


if __name__ == "__main__":
    main()
