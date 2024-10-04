print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("\n\n*******************WELCOME TO THE TREASURE ISLAND*******************")

print("Your mission is to find treasure\n\n")
side=input("Where do you want to go? Left or right? ")
sides=side.lower()
if sides=="left":
  print("You are safe,let's move ahead\n")
  river=input("There is a river. what do you want to do? swim or wait ")
  rivers=river.lower()
  if rivers=="swim":
    print("You survived\n")
    door=input("There are three doors which one you want to choose? yellow,blue,red ")
    doors=door.lower()
    if doors=="yellow":
      print("You died,there was fire,GAME OVER")
    elif doors=="blue":
      print("There was flood,You died,GAME OVER")
    else:
      print("There was treasure,You won")
    
  else:
    print("No one came to save you,GAME OVER")
    
  
else:
  print("You collided with a car,GAME OVER")
  