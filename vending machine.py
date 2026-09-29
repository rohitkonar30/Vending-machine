MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "Revenue":0
}
def ingredient(i):
    L=MENU[i]["ingredients"]
    print(L)
def payment(i):
    c=MENU[i]["cost"]
    print(c)
    p=float(input("Please pay the amount"))
    if p>c:
        print("Here is your balance",p-c)
        print("Thank you for your payment")
        resources["revenue"]+=c
        return True
    elif p==c:




on=True
s=input("Do you want to turn on the machine?(y/n)")
if s=="y":
    on=True
else:
    on=False
while on:
    print("Welcome to the vending machine!")
    print(MENU)
    i=input("What would you like? ")
    if i=="espresso":
        ingredient(i)

    break


