#Colour codes used later
re="\033[91m"
bl="\033[94m"
g="\033[92m"
yel="\033[93m"


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    },
    "Stock":{
        "Chips": {"cost":10,
                  "qty":10}},
    "chocolate":{"cost":5,
                 "qty":5},

}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Revenue":0,
}
def ingredient(i):
    r=MENU[i]["ingredients"]
    if resources["water"]<=r["water"]:

    try:
        resources["water"]-=r["water"]
        resources["milk"]-=r["milk"]
        resources["coffee"]-=r["coffee"]
    except:
        print("error call support")
#NEED to change


def payment(i):
    c=MENU[i]["cost"]
    print(c)
    p=float(input("Please pay the amount"))
    if p>=c:
        print("Here is your balance",p-c)
        print("Thank you for your payment")
        resources["revenue"]+=c
        return True
    else:
        print("\033[93m Pls enter the correct amount and retry the payment \033[0m")
        payment(i)
        return False

on=True
s=input("Do you want to turn on the machine?(y/n)\n")
if s=="y":
    on=True
else:
    on=False
while on:
    print("Welcome to the vending machine!")
    print(MENU)
    i=input("What would you like? \n")
    if i=="espresso":
        ingredient(i)
        payment(i) #change
        if payment(i):
            print("Here is your Drink 😎")
        else:
            print("do sgain")

    break


