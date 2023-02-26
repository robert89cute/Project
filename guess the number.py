import random

def guess_the_number():
    ranges = input("Type a number: ")# inputing the range

    if ranges.isdigit(): #if the ranges is digit is true
        ranges = int(ranges)# converting the variable into INT

        if ranges <= 0:
            print('Please type a number larger than 0 next time.')
            quit()
    else: #if the input ranges is not a digit this will execute
        print('Please type a number next time.')
        quit()

    random_number = random.randint(0, ranges)
    guesses = 0

    while True:
        guesses += 1
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print('Please type a number next time.')
            continue

        if user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

    print("You got it in", guesses, "guesses")

    yesorno = input('you wanna try again? SELECT (Y/N) Y for yes N for no: ')

    if yesorno.lower() == 'y':
                return guess_the_number()
            
    elif yesorno.lower() == 'n':
            print('Thank You!!!\n Goodbye! See You!!!')
    
guess_the_number()
