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
    # print 'Do you want to change a word? (y/n)'
    option = raw_input('Do you want to change a word? (y/n) ')
    if option is 'y' or 'Y':
        return True
    elif option is 'n' or 'N':
        return False


def monte_de_if(secret_word, letters_guessed, guesses, available):
    # guessed = show_hide_letters(secret_word, letters_guessed)
    letter = show_available_letters(available)

    if letter in letters_guessed:
        guessed = show_hide_letters(secret_word, letters_guessed)
        print 'Oops! You have already guessed that letter: ', guessed
        # answer = {'answer':'Oops! You have already guessed that letter: ' + guessed,  'guesses': guesses}
    elif letter in secret_word:
        letters_guessed.append(letter)

        guessed = show_hide_letters(secret_word, letters_guessed)
        print 'Good Guess: ', guessed
        # answer = {'answer': 'Good Guess: ' + guessed,  'guesses': guesses}
    else:
        guesses -= 1  # get_guesses(guesses)  # -= 1
        letters_guessed.append(letter)
        guessed = show_hide_letters(secret_word, letters_guessed)
        print 'Oops! That letter is not in my word: ', guessed
        return guesses
    return guesses
        # answer = {'answer': 'Oops! That letter is not in my word: ' + guessed, 'guesses': guesses}

        # return answer


def get_guesses(guesses):
    guesses = guesses - 1
    return guesses


"""
def get_guesses_2(guesses):
    g1 = 8
    guesses =
    return g1

    guesses = guesses - 1
    return guesses
"""


def show_available_letters(available):
    print 'Available letters', available
    letter = raw_input('Please guess a letter: ')
    return letter


def hangman(secret_word):

    guesses = 8
    letters_guessed = []

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secret_word), ' letters long.'
    print '-------------'

    available = get_available_letters()
    """
    count = remove_letters(available, secret_word)["count"]
    print 'There are ', count, 'letters differents.'

    if count > guesses:
        # while change_word
        change_word()
        while change_word() is True:
            secret_word = load_words().lower()
            hangman(secret_word)
            print '-------------'
            print change_word()
        else:
            pass
        # else:
    """

    while is_word_guessed(secret_word, letters_guessed) is False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        available = remove_letters(available, letters_guessed)["available"]
        """
        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        """
        # letter = show_available_letters(available)
        # guessed = show_hide_letters(secret_word, letters_guessed)

        guesses = monte_de_if(secret_word, letters_guessed, guesses, available)
        #guesses =
        #print answer
        #guesses = monte_de_if(secret_word, letters_guessed, letter, guesses)["guesses"]

        """
        if letter in letters_guessed:
            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secret_word:
            letters_guessed.append(letter)

            guessed = show_hide_letters(secret_word, letters_guessed)

            print 'Good Guess: ', guessed
        else:
            guesses -= 1
            letters_guessed.append(letter)

            print 'Oops! That letter is not in my word: ',  guessed
        """
        print '------------'

    else:
        if is_word_guessed(secret_word, letters_guessed) is True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secret_word, '.'


secret_word = load_words().lower()
hangman(secret_word)
