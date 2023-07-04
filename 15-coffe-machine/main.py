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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

expresso  = MENU['espresso']['ingredients']
latte  = MENU['latte']['ingredients']
cappuccino  = MENU['cappuccino']['ingredients']

def validations (choice):

    if choice == 'expresso':
        if resources['water'] < expresso['water']:
            print('Sorry there is not enough water.')
            return False
        elif resources['coffee'] < expresso['coffee']:
            print('Sorry there is not enough coffee.')
            return False
        
    if choice == 'latte':
        if resources['water'] < latte['water']:
            print('Sorry there is not enough water.')
            return False
        elif resources['coffee'] < latte['coffee']:
            print('Sorry there is not enough coffee.')
            return False
        elif resources['milk'] < latte['milk']:
            print('Sorry there is not enough milk.')
            return False
        
    if choice == 'cappuccino':
        if resources['water'] < cappuccino['water']:
            print('Sorry there is not enough water.')
            return False
        elif resources['coffee'] < cappuccino['coffee']:
            print('Sorry there is not enough coffee.')
            return False
        elif resources['milk'] < cappuccino['milk']:
            print('Sorry there is not enough milk.')
            return False
        
    return True

def processCoins( choice ):

    if not validations(choice=choice):
        return
        
    print('Please insert coins.')
    quartersChoice = int(input('How many quarters?: '))
    dimesChoice = int(input('How many dimes:? '))
    nicklesChoice = int(input('How many nickles?: '))
    penniesChoice = int(input('How many pennies?: '))

    quarterTotal = 0.25 * quartersChoice    
    dimesTotal =  0.10 * dimesChoice        
    nicklesTotal = 0.05 * nicklesChoice        
    penniesTotal = 0.01 * penniesChoice    

    totalList = [ quarterTotal, dimesTotal, nicklesTotal, penniesTotal ]
    total = sum( totalList )
    return total

def checkTransaction(choice):
    expressoCost  = MENU['espresso']['cost']
    latteCost  = MENU['latte']['cost']
    cappuccinoCost  = MENU['cappuccino']['cost']
    
    if choice == 'expresso':

        if expressoCost > processCoins(choice=choice):
            print("Sorry that's not enough money. Money refunded.")
            return

        resources['coffee'] = resources['coffee'] - expresso['coffee']
        resources['water'] = resources['water'] - expresso['water']
        resources['money'] = processCoins(choice=choice)

    elif choice == 'latte':
        if latteCost > processCoins(choice=choice):
            print("Sorry that's not enough money. Money refunded.")
            return

        resources['coffee'] = resources['coffee'] - latte['coffee']
        resources['milk'] = resources['milk'] - latte['milk']
        resources['water'] = resources['water'] - latte['water']
        resources['money'] = processCoins(choice=choice)

    elif choice == 'cappuccino':
        if cappuccinoCost > processCoins(choice=choice):
            print("Sorry that's not enough money. Money refunded.")
            return

        resources['coffee'] = resources['coffee'] - cappuccino['coffee']
        resources['milk'] = resources['milk'] - cappuccino['milk']
        resources['water'] = resources['water'] - cappuccino['water']
        resources['money'] = processCoins(choice=choice)
    

def report():
    print(f"Water: { resources['water']}ml ")
    print(f"Milk: { resources['milk']}ml ")
    print(f"Coffee: { resources['coffee']}g ")
    print(f"Money: $ { resources['money'] }")

def coffe_machine():
    should_run = True
    while should_run:
        print(resources)
        choice = input("What would you like? (expresso/latte/cappuccino): ").lower()
        if choice == 'expresso':
            checkTransaction(choice=choice)
        elif choice == 'latte':
            checkTransaction(choice=choice)
        elif choice == 'cappuccino':
            checkTransaction(choice=choice)
        elif choice == 'report':
            report()
        elif choice == 'off':
            should_run = False
        else:
            print('Choose a valid option')

coffe_machine()