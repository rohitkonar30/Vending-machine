from getpass import getpass
import time
#Colour codes used later
re="\033[91m"
bl="\033[94m"
g="\033[92m"
yel="\033[93m"
mg="\033[35m"
bol="\033[1m"
bgr="\033[41m"
rs="\033[0m"
#Password for admin access change it as per your requirement
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
        "chips": {"cost":10,
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
    time.sleep(0.5)
    for k,v in n.items():
        if resources[k]<v:
            print(f"{re}Sorry there is not enough {k}{rs}")
            time.sleep(0.5)
            print(f"{re}Please refill the machine{rs}")
            time.sleep(1)
            return False
    return True
def make(i):
    for k,v in MENU[i]["ingredients"].items():
        resources[k]-=v
    print(f"{g}Here is your {i} 😎{rs}")
    print(f"{g}Enjoy your {i}!{rs}")    

def payment(d,i):
    c=d[i]["cost"]
    print(f"The cost of {i} is ${c}")
    try:
        p=float(input("Please pay the amount\n"))
    except ValueError:
        print(f"{re}Invalid input. Please enter a valid amount.{rs}")
        q=input("Do you want to retry the payment? (y/n): ").lower()
        if q=="y":
            return payment(d,i)
        else:
            print(f"{re}Transaction Cancelled. Please try again later.{rs}")
            time.sleep(0.1)
            return False
    if p>=c:
        print(f"{g}Here is your balance {p-c}{rs}")
        print(f"{g}Thank you for your payment{rs}")
        print(f"Have a good day!😎")
        resources["revenue"]+=c
        return True
    else:
        print(f"{yel}Pls enter the correct amount and retry the payment{rs}")
        time.sleep(0.1)
        payment(d,i)
        return False

on=True
s=input("Do you want to turn on the machine?(y/n)\n").lower()
if s=="y":
    on=True
else:
    on=False
while on:
    print("Welcome to the vending machine!")
    print(f"{g}The stock available is:{rs}")
    for k,v in Stock.items():
        print(f"{bl}{k}: {v['qty']} {rs}")
    print("The available drinks are:")
    for k,v in MENU.items():
        print(f"{bl}{k}: ${v['cost']} {rs}")    
#    print(MENU)
    i=input("What would you like? \n").lower()
    if i in MENU.keys():
        if chk(i):
            p=payment(MENU,i)
            if p:
                make(i)
                time.sleep(2)
            else:
                print(f"{re}Try again later{rs}")
                time.sleep(0.5)
                pass
        time.sleep(1)    
    elif i in Stock.keys():
        if Stock[i]["qty"]>0:
            p=payment(Stock,i)
            if p:
                Stock[i]["qty"]-=1
                time.sleep(2)
                print(f"{g}Here is your {i} 😎{rs}")
                time.sleep(2)
                print(f"{g}Enjoy your {i}!{rs}")
                time.sleep(2)
            else:
                print(f"{re}Try again later{rs}")
                time.sleep(0.5)
        else:
            print(f"{re}Sorry, {i} is out of stock{rs}")
            time.sleep(0.5)
            print(f"{re}Please restock the machine{rs}")
            print(f"{bl}Sorry for the inconvenience{rs}")       
        time.sleep(1)     
    elif i=="e000":
        resources["water"]=0
        resources["milk"]=0
        resources["coffee"]=0
        time.sleep(2)
        print(f"{yel}The machine has been reset{rs}")
        time.sleep(0.5)
    elif i=="report":
        print(f"The resources available are:")
        for k,v in resources.items():
            print(f"{bl} {k}:{v} {rs}")
        time.sleep(3)    
    elif i=="off":
        print(f"{re}The machine has been turned off{rs}")
        on=False
        print(f"{g}Thank you for using the vending machine!{rs}")
        time.sleep(0.5)
    elif i=="fill":
        resources["water"]+=int(input("Enter the amount of water to refill: "))
        resources["milk"]+=int(input("Enter the amount of milk to refill: "))
        resources["coffee"]+=int(input("Enter the amount of coffee to refill: "))
        time.sleep(0.5)
        print(f"{g}The machine has been refilled Successfully{rs}")
        time.sleep(0.5)
    elif i=="main":
        p=getpass("Enter authentication password: ")
        if p==Admin_pass:
            print(f"{g}Authentication successful{rs}")
            time.sleep(0.5)
            print(f"\n{bgr}{bl}{bol} ⚠️  WARNING: ADMIN MODE ACTIVE   {rs}\n")
            time.sleep(0.5)
            print(f"{mg}{bol}[Access Granted]:{rs} You are logged in with {re}Administrator{rs} privileges.\n")
            a=True
        else:
            print(f"{re}Authentication failed{rs}")
            time.sleep(0.5)
            print(f"{mg}{bol}[Access Denied]:{rs} You do not have the necessary permissions to access this section.\n")
            a=False
        while a:
            print(f"{mg}Welcome to the Admin Menu{rs}")
            print(f"{mg}1. Collect revenue {rs}")
            print(f"{mg}2. Add Stock{rs}")
            print(f"{mg}3. Remove Stock{rs}")
            print(f"{mg}4. Exit Admin Menu{rs}")
            choice=input("Enter your choice: ")
            if choice=="1":
                print(f"{g}The revenue collected is: ${resources['revenue']}{rs}")
                print(f"{g}Transferring the money...{rs}")
                time.sleep(2)
                print(f"{g}Please collect the money{rs}")
                resources["revenue"]=0
                print(f"{g}Transaction successfull {rs}")
                time.sleep(0.5)
            elif choice=="2":
                item=input("Enter the item name to add stock: ").lower()
                qty=int(input("Enter the quantity to add: "))
                if item in Stock:
                    Stock[item]["qty"]+=qty
                    print(f"{g}Stock added successfully{rs}")
                else:
                    cost=float(input("Enter the cost of the item: "))
                    Stock[item]={"cost":cost,"qty":qty}
                    print(f"{g}New item added successfully{rs}")
            elif choice=="3":
                item=input("Enter the item name to remove stock: ")
                qty=int(input("Enter the quantity to remove: "))
                if item in Stock:
                    if Stock[item]["qty"]>=qty:
                        Stock[item]["qty"]-=qty
                        print(f"{g}Stock removed successfully{rs}")
                    else:
                        print(f"{re}Not enough stock available{rs}")
                else:
                    print(f"{re}Item not found in stock{rs}")
            elif choice=="4":
                a=False
                print(f"{g}Exiting Admin Menu{rs}")
                time.sleep(2)
                print(f"{mg}Returning to main menu...{rs}")
                time.sleep(0.5)
                print(f"Have a good day!😎")
            else:
                print(f"{re}Invalid choice, please try again{rs}")
    else:
        time.sleep(0.5)
        print(f"{yel}WARNING:The item you have selected is not available{rs}")
        time.sleep(2)