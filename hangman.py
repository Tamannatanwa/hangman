import random
list_word=["navgurukul","python","module","tamanna"]
secrect_word=random.choice(list_word)
def hangman(secrect_word):
    print ("I am thinking of a word that is " + str(len(secrect_word)) + " letters long.")
    turns=10
    guessword=""
    valid_entry=set("abcdefghijklmnopqrstuvwxyz")
    while len(secrect_word)>0:
        main_word=""
        # missed=0
        for letter in secrect_word:
            if letter in guessword:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "
        if main_word==secrect_word:
            print(main_word)
            print("YOU WON")
            print (" * * Congratulations, you won! * * ")
            break
        print("guess the word",main_word)
        guess=input("enter guessing word:-")
        if guess in valid_entry:
            guessword+=guess
        else:
            print("enter the valid character:-")
        if guess not in secrect_word:
            turns=turns-1
            if turns==9:
                print("9 turns left!!!")
                print("--------------")
            if turns==8:
                print("8 turns left!!!")
                print("--------------")
                print("     o     ")
            if turns==7:
                print("7 turns left!!!")
                print("--------------")
                print("     o     ")
                print("     |     ")
            if turns==6:
                print("6 turns left!!!")
                print("--------------")
                print("     o     ")
                print("     |     ")
                print("    /      ")
            if turns==5:
                print("5 turns left!!!")
                print("--------------")
                print("     o     ")
                print("     |     ")
                print("    / \    ")
            if turns==4:
                print("4 turns left!!!")
                print("--------------")
                print("    \o     ")
                print("     |     ")
                print("    / \    ")
            if turns==3:
                print("3 turns left!!!")
                print("--------------")
                print("    \o/     ")
                print("     |     ")
                print("    / \    ")
            if turns==2:
                print("2 turns left!!!")
                print("--------------")
                print("    \o/ |   ")
                print("     |     ")
                print("    / \    ")
            if turns==1:
                print("only last turn left!!!1hangman on his last breath")
                print("--------------")
                print("    \o/_|   ")
                print("     |     ")
                print("    / \    ")
            if turns==0:
                print("YOU LOSS!!","secret word is",secrect_word)
                print("you let a good man die")
                print("--------------")
                print("     o_|   ")
                print("    /|\    ")
                print("    / \    ")
                break
name=input("enter your name....")
print ("Welcome to the game, Hangman!",name)
print("YOU HAVE 10 CHANGE FOR GUSSING CARECT WORD! ")
hangman(secrect_word)


