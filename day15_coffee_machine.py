MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,

        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

order=True

resources["money"]=0
def enter_coins(item):
    actual_cost=MENU[item]["cost"]
    water=MENU[item]["ingredients"]["water"]
    milk=MENU[item]["ingredients"]["milk"]
    coffee=MENU[item]["ingredients"]["coffee"]

    quarters = int(input("Enter quarters"))
    dimes = int(input("Enter dimes"))
    nickle = int(input("Enter nickle"))
    pennies = int(input("Enter pennies"))
    total= quarters * 0.25 + dimes * 0.10 + nickle * 0.05 + pennies * 0.01
    if total < actual_cost:
        print("Sorry not enough money . Money refunded")
    elif total >= actual_cost:
        if total > actual_cost:
           chang = total - actual_cost
           change=round(chang, 4)
           print(f"your change is ${change}. ")
        resources["money"] += actual_cost
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee

        print(f"Here's your {item}!. Enjoy")



def check_resources(item):
    for resource in MENU[item]["ingredients"]:
        if resources[resource] < MENU[item]["ingredients"][resource]:
            print(f"Sorry not enough {resource}")
            return
    enter_coins(item)

    # if resources["water"] < MENU[item]["ingredients"]["water"]:
    #     print("Sorry not enough water")
    # elif resources["coffee"] < MENU[item]["ingredients"]["coffee"] :
    #     print("Sorry not enough coffee")
    # elif resources["milk"] < MENU[item]["ingredients"]["milk"]:
    #     print("Sorry not enough milk")
    # else:
    #     enter_coins(item)




while (order) :
    customer_chose = input("What would you like? (espresso/latte/cappuccino):")
    if customer_chose=='off':
        order=False
    elif customer_chose == "report":
        print(resources)
    elif customer_chose == 'espresso':
        check_resources('espresso')
    elif customer_chose == "latte":
        check_resources('latte')
    elif customer_chose == "cappuccino":
        check_resources('cappuccino')
    else:
        print("We don't have this :( ")




