import random
import string

from words import words


def get_valid_word(w):
    word = random.choice(words)  # this method randomly chooses an element from the sequence. (list in this case)
    while '-' in word or ' ' in word:
        word = random.choice(w)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # creates a set object. eg- if word = apple then word_letters = {a,p,l,e} (unordered)
    # set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements, commonly called Set.
    albhabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used.
        # '$'.join(['a', 'b', 'cf']) --> "a$b$cf"
        print("You have", lives, "lives left and you have used these letters: ", ' '.join(used_letters))

        # what current word is (eg W - R D)

        # word_list = []
        # for letter in word:
        #     if letter in used_letters:
        #         word_list.append(letter)
        #     else:
        #         word_list.append('-')

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print("Current word: ", ' '.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in albhabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 # takes away a life if wrong
                print("Letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please  try again.")

    # gets here when len(word_letter) == 0 or lives == 0
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word", word,"!")

hangman()

