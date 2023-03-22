import random
from words import words #importing the words file which contains a list of random words
import string

def extract_correct_word(words):
    word = random.choice(words) #randomly choose the any word from the word list
    while '-' in word or ' ' in words:  #this will help us to select just the words ignoring all the symbols
        word = random.choice(words)

    return word.upper()

def hangman():
    word =extract_correct_word(words)
    letters_in_word =set(word)  #letters in the word
    alphabet = set(string.ascii_uppercase) #all the ascii alphabets would be converted to uppercase
    guessed_letters = set()  #what the user has guessed

    attempts = len(letters_in_word) + 2   #setting the number of attemp user can play


    #getting user input
    while len(letters_in_word) >0 and attempts > 0:
        #letter used
        # ' '.join(['a','b','cd']) --> 'a b cd'
        print('You have',attempts,'attempts left and You have used these letters: ', ' '.join(guessed_letters))   #opening setence which shows the remaing attempts with all the characters we have entered


        #what current word is (i.e W - R D)
        actual_word_list = [letter if letter in guessed_letters else '-' for letter in word]  #will present the actual word with correct guessed alphabets or - is not yet guessed
        print('Current word: ', ' '.join(actual_word_list))

        guessed_letter_list = input('Guess a letter:').upper()   #taking the used input
        if guessed_letter_list in alphabet - guessed_letters:  #if the alphabet entered is new one it would be added to the guessed_letter_lists list
            guessed_letters.add(guessed_letter_list)
            if guessed_letter_list in letters_in_word:     #if the guessed alphabet is the correct word then we will remove it from the letters_in_word list which contain the correct word 
                letters_in_word.remove(guessed_letter_list)

            else:
                attempts = attempts - 1 # takes away one life if guessed wrong
                print ('Letter is not in the word.')


        elif guessed_letter_list in guessed_letters:   #if the guessed word is already is the guessed word list of used letters then computer will have to ask us again 
            print('You have already used that character. Please try again.')
        
        else:
            print('invalid character. please try again.')

    #get here when len(letters_in_word)== 0 or when attempts ==0
    if attempts ==0:
        print('You died,Sorry. The word was ', word)
    else:
        print('You guessed the word', word, '!!')


hangman()



 