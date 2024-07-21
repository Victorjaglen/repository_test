TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

def total_price(confirmation):
    return  confirmation * TICKET_PRICE + SERVICE_CHARGE

while tickets_remaining > 0:
    user_name = input('Welcome, whats your name loser??   ')
    print('Hello {} , Welcome to the booking system Currently there are {} tickets remaining'.format(user_name, tickets_remaining))

    try: 
        confirmation = int(input('{} Please confirm how many tickets would you like to buy? '.format(user_name)))
        if confirmation > tickets_remaining:
            raise ValueError('{}, There are only {} tickets remaining we do not have that many tickets available PTA'.format(user_name, tickets_remaining))
    except ValueError as err:
        print('{}'.format(err))

    else:
        total_cost = confirmation * TICKET_PRICE

        purchase_confirmation = input(' {} The total price for {} tickets will be {}. Please confirm if you would like to buy, by writing yes/no '.format(user_name, confirmation, total_price(confirmation)))


        if purchase_confirmation.lower() == 'yes':
            print('Tickets confirmed, see you at the show')
            tickets_remaining -= confirmation


        else:
            print('Thanks for checking out, {} Let us know if you want to purchase the tickets'.format(user_name))
print('Sold OUT')