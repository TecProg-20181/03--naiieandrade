import random
import string

WORDLIST_FILENAME = "palavras.txt"


class Word:
    def __init__(self):
        self.word = self.return_word()

    def load_words(self):
        """Depending on the size of the word list, this function may
        take a while to finish.
        """
        print "Loading word list from file..."
        in_file = open(WORDLIST_FILENAME, 'r')
        line = in_file.readline()
        wordlist = string.split(line)
        print "  ", len(wordlist), "words loaded."
        return wordlist

    def return_word(self):
        """Choose the word randomly from wordlist"""
        wordlist = self.load_words()
        word = random.choice(wordlist)
        return word


class Game(object):
    word = Word()

    def is_word_guessed(self, secret_word, letters_guessed):
        """Check letter guessed in secret word.
        Parameters: secret_word:string, letters_guessed:list
        return: boolean"""

        for letter in secret_word:
            if letter in letters_guessed:
                pass
            else:
                return False
        return True

    def remove_letters(self, available, word):
        """Remove repeated letters and count different letters.
        Parameters: available: , word:string -> return dictionary[integer, ]"""
        count_different_letters_in_word = 0

        for letter in available:
            if letter in word:
                count_different_letters_in_word += 1
                available = available.replace(letter, '')
            else:
                pass
        dic = {'count': count_different_letters_in_word, 'available': available}
        return dic

    def show_hide_letters(self, secret_word, letters_guessed):
        """Show letters guessed and hide other letters.
        Parameters: secret_word:string, letters_guessed:list
        return guessed:string"""
        guessed = ''

        for letter in secret_word:
            if letter in letters_guessed:
                guessed += letter
            else:
                guessed += '_ '

        return guessed

    def change_word(self):

        option = raw_input('Do you want to change a word? (y/n) ')
        option = option.lower()
        while option not in {'y', 'n'}:
            print 'Invalid input. Try again.'
            option = raw_input('Do you want to change a word? (y/n) ')
            option = option.lower()
        if option == 'y':
            return True
        elif option == 'n':
            return False

    def while_guesses_is_greater(self, secret_word, letters_guessed,
                                 guesses, available, letter):

        if letter in letters_guessed:
            guessed = self.show_hide_letters(secret_word, letters_guessed)
            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secret_word:
            letters_guessed.append(letter)
            guessed = self.show_hide_letters(secret_word, letters_guessed)
            print 'Good Guess: ', guessed
        elif letter == 'tip':
            pass
        else:
            guesses -= 1
            letters_guessed.append(letter)
            guessed = self.show_hide_letters(secret_word, letters_guessed)
            print 'Oops! That letter is not in my word: ', guessed
            return guesses
        return guesses

    def get_input_letter(self, available):

        while True:
            print 'Available letters', available
            letter = raw_input('Please guess a letter: ')
            letter = letter.lower()
            if len(letter) == 1:
                if letter in string.letters:
                    break
                print '!!! Please enter only letters'
            else:
                if letter == 'tip':
                    break
                print '!!! Please enter only one letter'
        return letter

    def option_to_change_word(self, secret_word, count):
        """If size of word is bigger than guesses, ask if want to change a word.
        Parameters: secret_word:string, count:integer"""
        if count > 8:
            if self.change_word() is True:
                print '####################'
                secret_word = self.word.return_word().lower()
                self.show_size_secret_word(secret_word)
                self.guess_the_word(secret_word)
                exit()
            else:
                pass

    def show_tip(self, letter, available, secret_word):
        if letter == 'tip':
            count = self.remove_letters(available, secret_word)["count"]
            print '<o/      There are ', count, 'letters differents.'
            self.option_to_change_word(secret_word, count)

    def guess_the_word(self, secret_word):
        guesses = 8
        letters_guessed = []
        # Importing letter of alphabet 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        while self.is_word_guessed(secret_word, letters_guessed) is False and guesses > 0:
            print 'You have ', guesses, 'guesses left.'

            available = self.remove_letters(available, letters_guessed)["available"]
            letter = self.get_input_letter(available)
            self.show_tip(letter, available, secret_word)

            guesses = self.while_guesses_is_greater(secret_word, letters_guessed, guesses, available, letter)

            print '------------'

        else:
            if self.is_word_guessed(secret_word, letters_guessed) is True:
                print 'Congratulations, you won!'
            else:
                print 'Sorry, you ran out of guesses. The word was ', secret_word, '.'

    def show_size_secret_word(self, secret_word):
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(secret_word), ' letters long.'
        print 'If you want a tip, write tip'
        print '-------------'

    def hangman(self):
        secret_word = self.word.word.lower()
        self.show_size_secret_word(secret_word)
        self.guess_the_word(secret_word)


game = Game()
game.hangman()
