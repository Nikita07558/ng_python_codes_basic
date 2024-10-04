#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
#from art import logo

number = random.randint(1, 100)
game = False
#print(logo)
print(
    'Welcome to number guess game : In this game you need to guess a number between 1 and 100\n'
)
level = input("Choose Difficulty level:- 'hard' or 'easy'? ").lower()
if (level == 'hard'):
    lives = 5
    print("You have 5 lives to complete the challenge\n")
elif (level == 'easy'):
    lives = 10
    print("You have 10 lives to complete the challenge\n")
else:
    print("wrong")
    game = True


def livesCheck():
    global lives
    print(f"Your lives are {lives-1} ")
    if (lives == 1):
        print("YOU LOST")
        global game
        game = True
    return lives - 1


while (not game):

    guess = int(input("\nGuess a number:- "))
    if (guess > number):
        print("Too high")
        lives = livesCheck()

    elif (guess < number):
        print("Too low")
        lives = livesCheck()

    else:
        print("YOU GUESSED CORRECT!!!")
        game = True
