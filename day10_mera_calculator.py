def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

operation= { "+" : add , "-" : subtract ,"*": multiply, "/":divide}

def calculator():
  
  program=True
  
  num1=float(input("What's the first number? "))
  for symbol in operation:
    print(symbol)
  while program:
    operate=input("Pick a symbol for the operation ? ")
    num2=float(input("What's the next number? "))
    function=operation[operate]
    value=function(num1,num2)
    print(f"{num1} {operate} {num2} = {value}\n" )
    
    next=input(f"Do you want to perform more operation on this {value} ? Type:-'yes' or Want to start a new calculation ?  Type :-'no' .").lower()
    if next=="no":
        program=False
        # clear()
        calculator()
      
    else:
        num1=value  
      
  print(value)    
    
  