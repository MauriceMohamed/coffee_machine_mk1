#coffee machine

choice = ""

#ressources variables
water = 0
milk = 0
coffee = 0
money = 0
real_bank = 0
bank= 0

choice1 = "espresso : $1.50"
choice2 = "latte : $2.50"
choice3 = "cappuccino : $3.00"

#define coffee prices
coffee_prices = {
"espresso" : 1.50,
"latte" : 2.50,
"cappuccino" : 3.00,
}

#define coin vaLue
coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

#define refilling function
def refill_water():
    global water
    water = water + 300
    print("The water is now full")

def refill_milk():
    global milk
    milk = milk + 200
    print("The milk is now full")

def refill_coffee():
    global coffee
    coffee = coffee + 100
    print("The coffee is now full")

def take_money():
    global money,bank
    bank += money
    money = 0
    print("You have taken all your money")

#define the coffees

def espresso():
    global water, milk, coffee, money
    water = water - 50
    coffee = coffee - 18
    print("*********************************************************")
    print("I have enough resources, making you a espresso!")
    print("enjoy your coffee!")
    print("*********************************************************")
def latte():
    global water, milk, coffee, money
    water = water - 200
    milk = milk - 150
    coffee = coffee - 24
    print("*********************************************************")
    print("I have enough resources, making you a latte!")
    print("enjoy your coffee!")
    print("*********************************************************")

def cappuccino():
    global water, milk, coffee, money
    water = water - 250
    milk = milk - 100
    coffee = coffee - 24
    print("*********************************************************")
    print("I have enough resources, making you a capuccino!")
    print("enjoy your coffee!")
    print("*********************************************************")

def not_enough_money():
    print("*********************************************************")
    print("Sorry, not enough money")
    print("*********************************************************")

def not_enough_milk():
    print("*********************************************************")
    print("Sorry, not enough milk")
    print("call the barista")
    print("*********************************************************")

def not_enough_water():
    print("*********************************************************")
    print("Sorry, not enough water")
    print("call the barista")
    print("*********************************************************")

def not_enough_coffee():
    print("*********************************************************")
    print("Sorry, not enough coffee")
    print("call the barista")
    print("*********************************************************")






#menu function
#loop for the menu
def menu():
    global choice
    print("*********************************************************")
    print("Coffee machine, Barista 5000")
    print("*********************************************************")
    print("1. Buy a coffee")
    print("2. Take a look at the stock")
    print("3. Take a look the cash")
    print("4. Quit")
    print("*********************************************************")
    print("What do you want to do? ")
    print("*********************************************************\n")
    choice = input()
    return choice

def buy_coffee():
    global choice, money
    print("*********************************************************")
    print("Credit {}".format(money))
    print("What do you want to buy? ")
    print("1. Espresso $1.50")
    print("2. Latte $2.50")
    print("3. Cappuccino $3.00")
    print("4. Back to main menu")
    print("*********************************************************")
    choice = input()
    return choice


def stock():
    global water, milk, coffee, money, choice
    print("*********************************************************")
    print("The coffee machine has:")
    print("{} of water".format(water))
    print("{} of milk".format(milk))
    print("{} of coffee beans".format(coffee))
    print("{} of money".format(money))
    print("*********************************************************")
    print("What do you want to do? ")
    print("1. Refill the water")
    print("2. Refill the milk")
    print("3. Refill the coffee beans")
    print("4. Back to main menu")
    print("*********************************************************")
    choice = input()
    return choice


def take_money():
    global money,bank,choice
    print("*********************************************************")
    print("The coffee machine has:")
    print("${}".format(bank))
    print("*********************************************************")
    print("Bank the money? y/n ")
    print("*********************************************************\n")
    choice = input()
    return choice

def add_coins():
    global money,bank,choice
    print("*********************************************************")
    print("The coffee machine has:")
    print("${}".format(round(money,2)))
    print("*********************************************************")
    print("1. Add a penny?")
    print("2. Add a dime?")
    print("3. Add a nickel?")
    print("4. Add a quarter?")
    print("5. Exit")
    print("*********************************************************\n")
    choice = input()
    return choice
def after_purchase():
    global money,bank,choice
    print("*********************************************************")
    print("Thank you for your purchase")
    print("The coffee machine has:")
    print("{} of water".format(water))
    print("{} of milk".format(milk))
    print("{} of coffee beans".format(coffee))
    print("{} of money".format(money))
    print("*********************************************************")
    print("What do you want to do? ")
    print("1. Main menu")
    print("2. Take a take your change")
    print("3. Quit")
    print("*********************************************************")
    choice = input()
    return choice


#####################programme############################

while True:
    menu()
    if choice == "1":
        buy_coffee()
        if choice == "1":
            if water < 50:
                print("*********************************************************")
                print("!!!!!!!!Sorry, not enough water!!!!!!!!!")
                print("call the barista")
                continue
            elif coffee < 18:
                print("*********************************************************")
                print("!!!!!!!!Sorry, not enough coffee beans!!!!!!!!!!")
                print("call the barista")
                continue
            else:
                while money != coffee_prices["espresso"]+1:
                    if float(money) < coffee_prices["espresso"]:
                        print("*********************************************************")
                        print("price : ${}".format(round(coffee_prices["espresso"],2)))
                        add_coins()
                        if choice == "1":
                            money = money + coins["penny"]
                        elif choice == "2":
                            money = money + coins["dime"]
                        elif choice == "3":
                            money = money + coins["nickel"]
                        elif choice == "4":
                            money = money + coins["quarter"]
                        elif choice == "5":
                            break
                        else:
                            print("Invalid input")
                    else:
                        change = money - coffee_prices["espresso"]
                        espresso()
                        money = money - coffee_prices["espresso"]
                        bank = bank + coffee_prices["espresso"]
                        after_purchase()
                        if choice == "1":
                            break
                        elif choice == "2":
                            print("*********************************************************")
                            print("here is your change ${}".format(round(change, 2)))
                            print("*********************************************************")
                            break
                        elif choice == "3":
                            break
                        else:
                            print("Invalid input")
                            break

        elif choice == "2":
                if water < 200:
                    print("*********************************************************")
                    print("!!!!!!!!Sorry, not enough water!!!!!!!!!")
                    print("call the barista")
                    continue
                elif milk < 150:
                    print("*********************************************************")
                    print("!!!!!!!!Sorry, not enough milk!!!!!!!!!")
                    print("call the barista")
                    continue
                elif coffee < 24:
                    print("*********************************************************")
                    print("!!!!!!!!Sorry, not enough coffee beans!!!!!!!!!")
                    print("call the barista")
                    continue
                else:
                    while money != coffee_prices["latte"]+1:
                        if float(money) < coffee_prices["latte"]:
                            print("*********************************************************")
                            print("price : ${}".format(round(coffee_prices["latte"],2)))
                            add_coins()
                            if choice == "1":
                                money = money + coins["penny"]
                            elif choice == "2":
                                money = money + coins["dime"]
                            elif choice == "3":
                                money = money + coins["nickel"]
                            elif choice == "4":
                                money = money + coins["quarter"]
                            elif choice == "5":
                                break
                            else:
                                print("Invalid input")
                        else:
                            change = money - coffee_prices["latte"]
                            latte()
                            money = money - coffee_prices["latte"]
                            bank = bank + coffee_prices["latte"]
                            after_purchase()
                            if choice == "1":
                                break
                            elif choice == "2":
                                print("*********************************************************")
                                print("here is your change ${}".format(round(change, 2)))
                                print("*********************************************************")
                                break
                            elif choice == "3":
                                break
                            else:
                                print("Invalid input")
        elif choice == "3":
                if water < 250:
                    print("*********************************************************")
                    print("!!!!!!!!Sorry, not enough water!!!!!!!!!")
                    print("call the barista")
                    continue
                elif milk < 100:
                    print("*********************************************************")
                    print("!!!!!!!!Sorry, not enough milk!!!!!!!!!")
                    print("call the barista")
                    continue
                elif coffee < 24:
                    print("*********************************************************")
                    print("!!!!!!!!Sorry, not enough coffee beans!!!!!!!!!")
                    print("call the barista")
                    continue
                else:
                    while money != coffee_prices["cappuccino"]+1:
                        if money < coffee_prices["cappuccino"]:
                            print("*********************************************************")
                            print("price : ${}".format(round(coffee_prices["cappuccino"],2)))
                            add_coins()
                            if choice == "1":
                                money = money + coins["penny"]
                            elif choice == "2":
                                money = money + coins["dime"]
                            elif choice == "3":
                                money = money + coins["nickel"]
                            elif choice == "4":
                                money = money + coins["quarter"]
                            elif choice == "5":
                                break
                            else:
                                print("Invalid input")
                        else:
                            change = money - coffee_prices["cappuccino"]
                            cappuccino()
                            money = money - coffee_prices["cappuccino"]
                            bank = bank + coffee_prices["cappuccino"]
                            after_purchase()
                            if choice == "1":
                                break
                            elif choice == "2":
                                print("*********************************************************")
                                print("here is your change ${}".format(round(change, 2)))
                                print("*********************************************************")
                                break
                            elif choice == "3":
                                break
                            else:
                                print("Invalid input")
        elif choice == "4":
            continue
        else:
            print("Invalid choice")
    elif choice == "2":
        while True:
            stock()
            if choice == "1":
                if water == 300:
                    print("Water is full")
                else:
                    refill_water()
            elif choice == "2":
                if milk == 200:
                    print("Milk is full")
                else:
                    refill_milk()
            elif choice == "3":
                if coffee == 100:
                    print("Coffee is full")
                else:
                    refill_coffee()
            elif choice == "4":
                break
        else:
            print("Invalid choice")
    elif choice == "3":
        take_money()
        if choice.lower() == "y":
            real_bank = real_bank + bank
            bank = 0

            print("*********************************************************")
            print("Your Bank Account has now ${}".format(round(real_bank, 2)))
            print("*********************************************************")
        elif choice.lower == "n":
            continue
        else:
            print("Invalid choice")
    elif choice == "4":
        print("*********************************************************")
        print("ok, bye")
        print("*********************************************************")
        break
    else:
        print("Invalid choice")






