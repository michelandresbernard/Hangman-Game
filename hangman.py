from words_list import words
import random
import string
def get_word ():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return (word.upper())    

def game():
    word = list(get_word())
    chances = 10
    print (word)
    print ("Your word has",len(word), "letters")
    guessed_letters = []
    picks = []

    while chances > 0:
        
        guess = input("Guess a letter: ").upper()
        if guess in list(string.ascii_uppercase): 
            picks.append(guess)
            if guess in guessed_letters:
                print ("You already choose that letter, try again")               
            else:
                chances = chances -1
                if guess in word:
                    guessed_letters.append(guess)
                    print ("You're right!")
                    
                else:
                    print("Wrong!")

            if len(word) == len(guessed_letters):
                print (word)
                print ("You win!!!")
                break
                
        else:
            print ("Invalid character")
        
        print ("Picks:",(picks))
        word_display = [letter if letter in guessed_letters else "-" for letter in word]
        print (word_display)
        print ("You have ",chances,"chances left")
        if chances == 0:
            print ("You loose!")
            print ("Word was:",word)
            break
game()