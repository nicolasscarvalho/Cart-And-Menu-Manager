class ShowInput:

    def __init__(self):
        pass


    def show_order(self, cart, total_price):
        
        for item_cart in cart:
            print(f'{cart.title} ------- {cart.price}')

        print('----------------------------------------------')

        print(f'Total price: {total_price}')