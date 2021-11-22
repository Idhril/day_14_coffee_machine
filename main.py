import data


def resources_check(order):
    for ingredient in data.resources:
        if order == "espresso" and ingredient == "milk":
            pass
        else:
            menu_dish = data.MENU[order]['ingredients'][ingredient]
            if data.resources[ingredient] < menu_dish:
                print("Sorry, there's not enough resources.")
                return 1
            # print(f"{resources[ingredient]}, {menu_dish}")
    return 0


def coin_receiver():
    coins = {'pennies': 0, 'nickels': 0, 'dimes': 0, 'quarters': 0}
    for coin in coins:
        coins[coin] = float(input(f"How many {coin}?: "))
        # print(coins)
    return coins
    #         make it a library, not separate entities


def payment_calc(coins):
    payment_total = (coins['pennies'] * 0.01) + (coins['nickels'] * 0.05) + (coins['dimes'] * 0.1) + (coins['quarters'] * 0.25)
    return payment_total


def resources_subtractor(order):
    for resource in data.resources:
        if order == "espresso" and resource == "milk":
            pass
        else:
            ingredient = data.MENU[order]['ingredients'][resource]
            data.resources[resource] -= ingredient
    # print(resources)
    return data.resources


def refill():
    data.resources['water'] = 300
    data.resources['milk'] = 200
    data.resources['coffee'] = 100


def coffee_machine():
    should_continue = True
    money = 0
    while should_continue:
        user_order = input("What would you like? (espresso/latte/cappuccino): ")
        if user_order == 'off':
            should_continue = False
            return 0
        elif user_order == 'report':
            for key in data.resources:
                print(f"{key.capitalize()}: {data.resources[key]}")
            print(f"Money: ${money}")
            #         here we need to figure out how to wait foe user input and then continue to new user input
            input("Press any key to start again   ")
            #               curvy braces should go away!
            continue
        elif user_order == 'refill':
            data.resources = refill()
            continue
        elif user_order in data.MENU:
            #         function for resources check
            if resources_check(user_order) == 1:
                continue
            # receiving user_coins and calculating how much it is in $
            user_coins = coin_receiver()
            payment = payment_calc(user_coins)
#           compare payment with cost of a drink
            order_cost = data.MENU[user_order]["cost"]
            if payment < order_cost:
                # if insufficient - subtract from coins total
                print("Sorry, payment insufficient. Money returned. ")
                continue
            elif payment > order_cost:
                diff = payment - order_cost
                print(f"Here is ${diff:.2f} in charge")
                payment -= diff
            # coins_total = sum of dict in payment variable, need it for calculating сдача
            money += payment
#           starting to make coffee. First, subtract resources
            data.resources = resources_subtractor(user_order)
            print(f"Here is your {user_order}. Enjoy!")


coffee_machine()
