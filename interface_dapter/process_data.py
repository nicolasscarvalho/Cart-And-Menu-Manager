from entities.menu import Menu

class ProcessInput:

    def __init__(self):
        pass




    def get_cart(self, menu: Menu):
        
        cart = []

        for section in menu:
            for food_item in section.food_items:
                cart.append(food_item)

        return cart




    def get_total_price(self, cart):

        total_price = 0

        for item_cart in cart:
            total_price += item_cart.price

        return total_price