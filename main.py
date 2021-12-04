from Beverages import *
from Pastries import *
from random import *
from datetime import date, datetime

# list of items and the sizes available
price_coffee = [['Small', 12.50], ['Regular', 14.50], ['Tall', 16.50]]
price_tea = [['Small', 10.00], ['Regular', 11.00], ['Tall', 12.00]]
price_softdrinks = [['Small', 7.50], ['Regular', 8.50], ['Tall', 9.50]]
coffee = ['espresso', 'machiato', 'mocha', 'latte', 'americano']
tea = ['green tea', 'black tea', 'milk tea']
softdrinks = ['pepsi', 'coca-cola', 'mountain dew', 'sprite']
doughnuts = [['chocolate', 12.25], ['red velvet cake', 16.75], ['strawberry', 13.50]]
cupcakes = [['red velvet', 10.50], ['chocolate', 13.75], ['mocha', 14.25]]

print('''*********** WELCOME TO URBANBEANS CAFE **************''')
while True:
    place_order = input('Would you like to place an order?(yes/no)')
    final_order = []
    change = 0
    final_amount = 0

    if place_order.lower() == 'yes':

        while True:
            print('''ITEMS AVAILABLE:
            
            BEVERAGES:
            -COFFEE
            -TEA
            -SOFT DRINKS
            
            PASTRIES:
            -CUPCAKES
            -DOUGHNUTS''')
            item = input('-')
            print('======================================================')
            if 'coffee' in item.lower():
                print("LIST OF COFFEE DRINKS AVAILABLE:")
                for _ in coffee:
                    print(_.upper())
                while True:
                    item_name = input('Enter coffee you\'d like to have: ')
                    if item_name not in coffee:
                        print('Item not available :(')
                        continue
                    else:
                        break

                print('\nCUP SIZES AVAILABLE')
                for _ in price_coffee:
                    for j in _:
                        print(j, end='\t')
                    print()
                while True:
                    item_size = input('Enter cup size:')
                    if (item_size.lower() != 'small') and (item_size.lower() != 'tall') and (
                            item_size.lower() != 'regular'):
                        print('PLEASE ENTER A VALID SIZE FOR YOUR DRINK')
                        continue
                    else:
                        break
                price = 0
                for i in price_coffee:
                    if item_size.lower() == i[0].lower():
                        price = i[1]
                qty = int(input('How many cups of your drink would you like to order?'))
                final_amount += price * qty
                final_order.append(['coffee', item_name, price, item_size, qty])

            elif 'tea' in item.lower():
                print("LIST OF TEA DRINKS AVAILABLE:")
                for _ in tea:
                    print(_.upper())
                while True:
                    item_name = input('Enter tea you\'d like to have: ')
                    if item_name not in tea:
                        print('Item  not available :(')
                        continue
                    else:
                        break
                print('\nCUP SIZES AVAILABLE')
                for _ in price_tea:
                    for j in _:
                        print(j, end='\t')
                    print()
                while True:
                    item_size = input('Enter cup size:')
                    if (item_size.lower() != 'small') and (item_size.lower() != 'tall') and (
                            item_size.lower() != 'regular'):
                        print('PLEASE ENTER A VALID SIZE FOR YOUR DRINK')
                        continue
                    else:
                        break
                price = 0
                for i in price_tea:
                    if item_size.lower() == i[0].lower():
                        price = i[1]
                qty = int(input('How many cups of your drink would you like to order?'))
                final_amount += price * qty
                final_order.append(['tea', item_name, price, item_size, qty])

            elif 'soft drinks' in item.lower():
                print("LIST OF SOFT DRINKS DRINKS AVAILABLE:")
                for _ in softdrinks:
                    print(_.upper())
                while True:
                    item_name = input('Enter drink you\'d like to have: ')
                    if item_name not in softdrinks:
                        print('Item  not available :(')
                        continue
                    else:
                        break
                print('\nGLASSES AVAILABLE:')
                for _ in price_softdrinks:
                    for j in _:
                        print(j, end='\t')
                    print()
                while True:
                    item_size = input('Enter glass size:')
                    if (item_size.lower() != 'small') and (item_size.lower() != 'tall') and (
                            item_size.lower() != 'regular'):
                        print('PLEASE ENTER A VALID SIZE FOR YOUR DRINK')
                        continue
                    else:
                        break
                price = 0
                for i in price_softdrinks:
                    if item_size.lower() == i[0].lower():
                        price = i[1]
                qty = int(input('How many glasses of your drink would you like to order?'))
                final_amount += price * qty
                final_order.append(['softdrink', item_name, price, item_size, qty])

            elif 'cupcakes' in item.lower():
                print('LIST OF CUPCAKES AVAILABLE:')
                for i in cupcakes:
                    for _ in i:
                        print(str(_).upper(), end='\t')
                    print()
                while True:
                    item_name = input('Cupcake you\'d like to order: ')
                    if (item_name.lower() != 'red velvet') and (item_name.lower() != 'mocha') and (
                            item_name.lower() != 'chocolate'):
                        print('Item  not available :(')
                        continue
                    else:
                        break
                type = input('Would you prefer eggless or with egg?')
                price = 0
                for i in cupcakes:
                    if item_name.lower() == i[0].lower():
                        price = i[1]
                qty = int(input('How many pieces would you like to order? '))
                final_amount += price * qty
                final_order.append(['cupcakes', item_name, price, type, qty])

            elif 'doughnuts' in item.lower():
                print('LIST OF DOUGHNUTS AVAILABLE:')
                for i in doughnuts:
                    for _ in i:
                        print(str(_).upper(), end='\t')
                    print()
                while True:
                    item_name = input('Doughnut you\'d like to order: ')
                    if (item_name.lower() != 'red velvet cake') and (item_name.lower() != 'strawberry') and (
                            item_name.lower() != 'chocolate'):
                        print('Item  not available :(')
                        continue
                    else:
                        break
                while True:
                    type = input('Would like you\'re doughnut to be cream filled(+ 5.00) ?')
                    if type.lower() == 'yes':
                        type = 'cream filled'
                        break
                    elif type.lower() == 'no':
                        type = 'normal'
                        break
                    else:
                        continue
                price = 0
                for i in doughnuts:
                    if item_name.lower() == i[0].lower():
                        price = i[1]

                qty = int(input('How many pieces would you like to order? '))
                if type.lower() == 'cream filled':
                    final_amount += (price + 5) * qty
                else:
                    final_amount += price * qty

                final_order.append(['doughnuts', item_name, price, type, qty])


            else:
                print('INVALID INPUT')
                continue
            print('======================================================')
            n = input('Would you like to add another item to your list?(yes/no)')
            if n.lower() == 'yes':
                print('======================================================')
                continue
            elif n.lower() == 'no':
                break
        print('------------------------------------')
        print('TOTAL AMOUNT: ', final_amount + (0.05 * final_amount))
        while True:
            budget = int(input('BUDGET TO BE GIVEN: '))
            if budget < final_amount:
                print('~~~YOUR BUDGET IS LESS THE TOTAL AMOUNT TO BE PAID')
                continue
            else:
                break
        while True:  ##statements added
            option = input('WOULD YOU LIKE TO \'DINE IN\' OR \'TAKE AWAY\'?')
            if ('dine in' in option.lower()) or ('take away' in option.lower()):
                break
            else:
                print(('please enter a valid input'))
                continue
        print('\n********** BILL ***********')
        print('\t', option)
        total = 0
        count = 1
        print('DATE: ', date.today())
        print('TIME: ', datetime.now().strftime("%H:%M:%S"))  # prints the current date and time
        print('ORDER NO.: ', randint(1, 100))  # prints a random number in the range 1-100

        for i in final_order:
            print(count, end='- ')
            if i[0].lower() == 'coffee':
                item = i[1]
                price = i[2]
                size = i[3]
                qty = i[4]
                order = Coffee(item, budget, price, size,
                               qty)  # takes the objects (description of the item) as the arguments
                print(order.__str__())  # returns description of the items
                total += order.get_total()  # gets the total amount ot be paid for the item
                budget = order.get_change(
                    budget)  # returns the budget amount left after subtracting the total amount for the item

            elif i[0].lower() == 'tea':
                item = i[1]
                price = i[2]
                size = i[3]
                qty = i[4]
                order = Tea(item, budget, price, size, qty)
                print(order.__str__())
                total += order.get_total()
                budget = order.get_change(budget)

            elif i[0].lower() == 'softdrink':
                item = i[1]
                price = i[2]
                size = i[3]
                qty = i[4]
                order = Softdrinks(item, budget, price, size, qty)
                print(order.__str__())
                total += order.get_total()
                budget = order.get_change(budget)

            elif i[0].lower() == 'cupcakes':
                item = i[1]
                price = i[2]
                type = i[3]
                qty = i[4]
                order = Cupcakes(item, budget, price, type, qty)
                print(order.__str__())
                total += order.get_total()
                budget = order.get_change(budget)

            elif i[0].lower() == 'doughnuts':
                item = i[1]
                price = i[2]
                type = i[3]
                qty = i[4]
                order = Doughnuts(item, budget, price, type, qty)
                print(order.__str__())
                total += order.get_total(price, qty)
                budget = order.change(budget)
            count += 1
        vat = 0.05 * total
        print('\nTOTAL: $', total)
        print('  with Vat: $', total + vat)
        print('CHANGE: $', budget - vat, '\n***************************')

        print('PLEASE WAIT AT THE COUNTER, YOUR ORDER IS BEING PREPARED')
    elif place_order.lower() == 'no':

        print('**THANK YOU FOR CHOOSING URBANBEANS**\nWE HOPE THAT YOU HAVE A GREAT DAY TODAY :)')
        break
    else:
        print('INVALID INPUT')
