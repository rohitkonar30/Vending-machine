#Colour codes used later
from pickle import LIST


re="\033[91m"
bl="\033[94m"
g="\033[92m"
yel="\033[93m"
rs="\033[0m"

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
    "revenue":1000,
}
# def ingredient(i):
#     r=MENU[i]["ingredients"]
#     if resources["water"]<=r["water"]:

#     try: 
#         resources["water"]-=r["water"]
#         resources["milk"]-=r["milk"]
#         resources["coffee"]-=r["coffee"]
#     except:
#         print("error call support")
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
#s=input("Do you want to turn on the machine?(y/n)\n").lower()
# if s=="y":
#     on=True
# else:
#     on=False
while on:
    print("Welcome to the vending machine!")
#    print(MENU)
    i=input("What would you like? \n")
    if i=="espresso":
#        ingredient(i)
        payment(i) #change
        if payment(i):
            print("Here is your Drink 😎")
        else:
            print("do again")
    elif i=="e000":
        resources["water"]=0
        resources["milk"]=0
        resources["coffee"]=0
        print(f"{yel}The machine has been reset{rs}")
        print(f"{g}The revenue collected is: ${resources['revenue']}{rs}")
        print(f"{g}Money successfully transferred{rs}")
        resources["revenue"]=0
    elif i=="report":
        print(f"{bl}The resources available are: {*list(resources),}{rs}")
             


