import sys, time, os

quiz ='         "QUIZ GAME"\n"Guess and Type The Right Answer"\n'
for char in quiz:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.1)

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            return
        else:
            if attempt < 2:
                guess = input("Sorry wrong answer, Try again\nanswer: ")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )

score = 0
loading = '\n3.. 2.. 1..\n'

guess1 = ("\nWhich bear lives at the North Pole?:")
for char in guess1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.1)
guess12 = input('\nanswer: ')
check_guess(guess12, "polar bear")
os.system('cls')

guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the larget animal? ")
check_guess(guess3, "Blue Whale")
print("Your Score is "+ str(score))

 
