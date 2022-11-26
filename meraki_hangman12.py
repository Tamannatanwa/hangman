import random
import string
from images import IMAGES
def load_words():
    word_list=["navgurukul","kindness","learning"]
    return word_list
def choose_word():
    word_list=load_words()
    secret_word=random.choice(word_list)
    secret_word=secret_word.lower()
    return secret_word
def is_word_guessed(secret_word,letters_guessed):
    # a=letters_guessed,secret_word
    return False
def get_guessed_word(secret_word,letters_guessed):
    index=0
    guessed_word=""
    while (index<len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word+=secret_word[index]
        else:
            guessed_word+="_ "
        index+=1
    return guessed_word
def get_available_letters(letters_guessed):
    letters_left=string.ascii_lowercase
    return letters_left
def hangman(secret_word):
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    letters_guessed = []
    remaining_lives=8
    while (True):
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)
        guess = input("Please guess a letter: ")
        letter = guess.lower()
        if letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")
            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
                print ("")
                break
        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word,letters_guessed))
            letters_guessed.append(letter)
            print ("")
            get_guessed_word(secret_word, letters_guessed)
            print (IMAGES[(8-remaining_lives)])
            print ("Remaining Lives : ", remaining_lives)
            print ("")
            letters_guessed.append(letter)
            remaining_lives -= 1
            if remaining_lives==0:
                break
    print("sorry,you lose the game,the word was:-",secret_word)
secret_word=choose_word()
hangman(secret_word)

