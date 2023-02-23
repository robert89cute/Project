import random
import time
from tagalog_list import tagalogwords

name = input('Please Enter Your Name: ').upper()

time.sleep(1)
print('LOADING')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(.5)
print('WELCOME!!!!\nHELLO!, '+'"' + name.upper()+'"' +'! Lets Play the BITAY-MAN!!!\n')
time.sleep(1)

#randomly chooses something from the list
def getvalidword(tagalogwords):
    tagalog = random.choice(tagalogwords) 
    return tagalog

#main function
def bitayman():
    Tags = getvalidword(tagalogwords)
    Nahulaan = []
    buhay = 8

    while buhay > 0:
        won = 0
        
        for titik in Tags:
            if titik in Nahulaan:
                print(titik.upper(), end=' ')
                
            else:
                print('_',end=' ')
                won += 1
        
        if won == 0:

            print('\n***************************\nYou won!!!', name, '\n***************************\n')
            break
            

        guess = input('\nGuess the word\n\nEnter a letter: ')
        if guess in Nahulaan:
            print('Already Guess the letter')
        Nahulaan += guess
        print('The letters you use: ', ' '.join(Nahulaan).upper())
             
        if guess not in Tags:
            buhay -= 1
            if buhay == 7:
                print('Wrong Letter:', guess.upper())
                print('You have', + buhay, 'more guesses, Try another letter')
                print('"B"')
                print('The letters you use: ', ' '.join(Nahulaan).upper())
                print('\n')
            if buhay == 6:
                print('Wrong Letter:', guess)
                print('You have', + buhay, 'more guesses, Try another letter')
                print('"B I"')
                print('The letters you use: ', ' '.join(Nahulaan).upper())
                print('\n')
            if buhay == 5:
                print('Wrong Letter:', guess)
                print('You have', + buhay, 'more guesses, Try another letter')
                print('"B I T"')
                print('The letters you use: ', ' '.join(Nahulaan).upper())
                print('\n')
            if buhay == 4:
                print('Wrong Letter:', guess)
                print('You have', + buhay, 'more guesses, Try another letter')
                print('"B I T A"')
                print('The letters you use: ', ' '.join(Nahulaan).upper())
                print('\n')
            if buhay == 3:
                print('Wrong Letter:', guess)
                print('You have', + buhay, 'more guesses, Try another letter')
                print('"B I T A Y"')
                print('The letters you use: ', ' '.join(Nahulaan).upper())
                print('\n')
            if buhay == 2:
                print('Wrong Letter:', guess)
                print('You have', + buhay, 'more guesses, Try another letter')
                print('"B I T A Y M"')
                print('The letters you use: ', ' '.join(Nahulaan).upper())
                print('\n')
            if buhay == 1:
                print('Wrong Letter:', guess)
                print('You have', + buhay, 'more guesses, Try another letter')
                print('"B I T A Y M A"')
                print('The letters you use: ', ' '.join(Nahulaan).upper())
                print('\n')
            if buhay == 0:
                print('***************************\n"B I T A Y M A N"')
                print('***************************\nYou Lose!!!\n***************************')
                print('The Word is '+ '"' + Tags + '"\n***************************')
       
    yesorno = input('You wanna play again? SELECT (Y/N) Y for yes N for no: ')

    if yesorno.lower() == 'y':
                return bitayman()
            
    elif yesorno.lower() == 'n':
            print('Thank You!!!', name, '\nGoodbye! See You!!!')
    
bitayman()

