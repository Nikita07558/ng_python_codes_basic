# from replit import clear
#HINT: You can call clear() to clear the output in the console.
program=True
bid_dictionary={}
while program :
 name=input("what's your name? ")
 bid=int(input("Your bid? $"))
 bid_dictionary[name]=bid
 question=input("Are there more bidder? yes or no ").lower()
 if question=="no":
   program=False
 #else: 
  # clear()
final_name=''
max=0
for name in bid_dictionary:
  if bid_dictionary[name]>max:
    max=bid_dictionary[name]
    final_name=name
print(f"Highest bid is {max} of {final_name}.")
