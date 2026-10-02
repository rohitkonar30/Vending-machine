from getpass import getpass

#Colour codes used later
re="\033[91m"
bl="\033[94m"
g="\033[92m"
yel="\033[93m"
rs="\033[0m"
Admin_pass="admin@01#"
a=False
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
    "water":{
        "ingredients": {
            "water": 100,
            "milk": 0,
            "coffee": 0,
        },
        "cost": 1.0,
    }
}    
Stock={
        "Chips": {"cost":10,
                  "qty":10},
        "chocolate":{"cost":5,
                 "qty":5},
        "cookies":{"cost":15,
                   "qty":5},
        "soda":{"cost":20,
                "qty":30},
        "instant noodles":{"cost":30,
                         "qty":10},

}                 

resources = {
    "water": 300,
    "milk": 300,
    "coffee": 300,
    "revenue":1000,
}
def chk(i):
    n=MENU[i]["ingredients"]
    for k,v in n.items():
        if resources[k]<v:
            print(f"{re}Sorry there is not enough {k}{rs}")
            return False
    return True
def make(i):
    for k,v in MENU[i]["ingredients"].items():
        resources[k]-=v

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
        print(f"The resources available are:")
        for k,v in resources.items():
            print(f"{bl} {k}:{v} {rs}")
    elif i=="off":
        print(f"{re}The machine has been turned off{rs}")
        on=False
    elif i=="fill":
        resources["water"]+=int(input("Enter the amount of water to refill: "))
        resources["milk"]+=int(input("Enter the amount of milk to refill: "))
        resources["coffee"]+=int(input("Enter the amount of coffee to refill: "))
        print(f"{g}The machine has been refilled Successfully{rs}")
    elif i=="main":
        p=getpass.getpass("Enter authentication password: ")
        if p==Admin_pass:
            print(f"{g}Authentication successful{rs}")
            a=True
        else:
            print(f"{re}Authentication failed{rs}")
            a=False

    else:
        try:
            if chk(i):
                payment(i)
                if payment(i):
                    make(i)
                    print(f"{g}Here is your {i} 😎{rs}")
                else:
                    print(f"{re}Try again later{rs}")
                pass
        except KeyError:
            print(f"{yel}The item you have selected is not available{rs}")
    break         

