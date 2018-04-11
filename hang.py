import random
import string

WORDLIST_FILENAME = "palavras.txt"


def load_words():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):

    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False

    return True


def get_guessed_word():

    guessed = ''

    return guessed


def get_available_letters():
    """
    Importing letter of alphabet
    'abcdefghijklmnopqrstuvwxyz'
    """
    available = string.ascii_lowercase

    return available


def remove_letters(available, word):
    count_different_letters_in_word = 0

    for letter in available:
        if letter in word:
            count_different_letters_in_word += 1
            available = available.replace(letter, '')
        else:
            pass
    dic = {'count': count_different_letters_in_word, 'available': available}
    return dic


def show_hide_letters(secret_word, letters_guessed):
    guessed = get_guessed_word()

    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '_ '

    return guessed


def change_word():

    option = raw_input('Do you want to change a word? (y/n) ')
    if option == 'y':
        return True
    elif option == 'n':
        return False


def while_guesses_is_greater(secret_word, letters_guessed, guesses, available, letter):

    if letter in letters_guessed:
        guessed = show_hide_letters(secret_word, letters_guessed)
        print 'Oops! You have already guessed that letter: ', guessed
    elif letter in secret_word:
        letters_guessed.append(letter)
        guessed = show_hide_letters(secret_word, letters_guessed)
        print 'Good Guess: ', guessed
    else:
        guesses -= 1
        letters_guessed.append(letter)
        guessed = show_hide_letters(secret_word, letters_guessed)
        print 'Oops! That letter is not in my word: ', guessed
        return guesses
    return guesses


def show_available_letters(available):
    print 'Available letters', available
    letter = raw_input('Please guess a letter: ')
    return letter


def option_to_change_word(secret_word, count, continue_game):

    if count > 8 and continue_game is True:
        while change_word() is True:
            secret_word = load_words().lower()
            hangman(secret_word)
            # continue_game = False
            return False
        else:
            pass
        # return False


def get_count():
    available = get_available_letters()
    count = remove_letters(available, secret_word)["count"]
    return count


def hangman(secret_word):

    guesses = 8
    letters_guessed = []

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secret_word), ' letters long.'
    print '-------------'

    available = get_available_letters()

    count = remove_letters(available, secret_word)["count"]
    print 'There are ', count, 'letters differents.'
    continue_game = True
    continue_game = option_to_change_word(secret_word, count, continue_game)

    while is_word_guessed(secret_word, letters_guessed) is False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        available = remove_letters(available, letters_guessed)["available"]

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')

        guesses = while_guesses_is_greater(secret_word, letters_guessed, guesses, available, letter)

        print '------------'

    else:
        if is_word_guessed(secret_word, letters_guessed) is True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secret_word, '.'


secret_word = load_words().lower()
hangman(secret_word)
