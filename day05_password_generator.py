#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for n in range(0,nr_letters):
  index=random.randint(0,52)  #use index or use directly random.choice(letters)
  print(letters[index],end='')
for n in range(0,nr_symbols):
  index=random.randint(0,8)
  print(symbols[index],end='')
for n in range(0,nr_numbers):
  index=random.randint(0,10)
  print(numbers[index],end='')


print("\n\n\n\n") 
print("Difficult password:-\n\n\n")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list=[]
for n in range(0,nr_letters):
  index=random.randint(0,52)
  password_list.append(letters[index])  # or password_list+=letters[index]
for n in range(0,nr_symbols):
  index=random.randint(0,8)
  password_list.append(symbols[index]) #or password_list+=symbols[index]
for n in range(0,nr_numbers):
  index=random.randint(0,10)
  password_list.append(numbers[index]) #or password_list+=numbers[index]
print(password_list)

new=random.shuffle(password_list)   #to reorder a list

password=''
for words in password_list:
  password+=words
print(password)  
