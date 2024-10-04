from higher_lower_game_data import data
from higher_lower_art import logo, vs
#from replit import clear
import random


def higherLower():
  score = 0
  gameover = False
  print(logo)
  next = random.randint(0, 50)
  while (not gameover):

    num1 = next
    num2 = random.randint(0, 50)
    while (num1==num2):
      num2=random.randint(0,50)
    print(
      f"Compare A : {data[num1]['name']} , {data[num1]['description']} , from {data[num1]['country']} "
    )
    print(vs)
    print(
      f"Compare B : {data[num2]['name']} , {data[num2]['description']} , from {data[num2]['country']} "
    )
    # print(f" A:{Afollowing} , B:{Bfollowing} ")
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

    Afollowing = data[num1]['follower_count']
    Bfollowing = data[num2]['follower_count']

    if (Afollowing > Bfollowing):
      more = 'a'
    elif (Bfollowing > Afollowing):
      more = 'b'
      
    next = num2
    # clear()
    print(logo)
    if (guess == more):
      print("That's correct!")
      score += 1
      print(f"your score is : {score}\n\n")

    else:
      print(f"That's incorrect .You lose .Your final score is :{score}.\n")
      print('Game over')
      gameover = True


wannaplay = input("\n\nDO YOU WANT TO PLAY HIGHER LOWER GAME ? 'y' or 'n': ")
while (wannaplay == 'y'):
  higherLower()
  wannaplay = input("\n\nDO YOU WANT TO PLAY HIGHER LOWER GAME ? 'y' or 'n': ")
