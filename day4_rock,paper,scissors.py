rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("********************Welcome to the Rock,Paper and Scissors Game*******************\n")
chose=int(input("\nChoose 0 for Rock ,1 for scissors and 2 for paper.\n"))
list_obj=[rock,scissors,paper]
if chose <=2:
   print(f"\n\nYour Choice: \n\n{list_obj[chose]}\n\n")

   import random
   comp_chosen=random.randint(0,2)
   print(f"Comp Choice: \n\n{list_obj[comp_chosen]}\n\n")

   if comp_chosen==chose :
     print("Draw")
   elif comp_chosen==0 and chose==2:
     print("You Won")
   elif comp_chosen==1 and chose==0:
     print("You Won")
   elif comp_chosen==2 and chose==1:
     print("You Won")
   else:
     print("You Lose")
else:
  print("Wrong input")



