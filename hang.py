import random
import string

WORDLIST_FILENAME = "palavras.txt"


def load_words():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    secret_letters = []

#    for letter in secretWord:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

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


def count_letters(available, word, option):
    count_different_letters_in_word = 0

    for letter in available:
        if letter in word:
            count_different_letters_in_word += 1
            available = available.replace(letter, '')
        else:
            pass
    if option is 1:
        return count_different_letters_in_word
    elif option is 2:
        return available


def show_hide_letters(secret_word, letters_guessed):
    guessed = get_guessed_word()

    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '_ '

    return guessed


def hangman(secret_word):

    guesses = 8
    letters_guessed = []
    option_count_letters = 1
    option_available_letters = 2

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secret_word), ' letters long.'
    print '-------------'

    available = get_available_letters()

    count = count_letters(available, secret_word, option_count_letters)

    print 'There are ', count, 'letters differents.'

    while is_word_guessed(secret_word, letters_guessed) is False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        available = count_letters(available, letters_guessed, option_available_letters)

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
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

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if is_word_guessed(secret_word, letters_guessed) is True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secret_word, '.'


secret_word = load_words().lower()
hangman(secret_word)
