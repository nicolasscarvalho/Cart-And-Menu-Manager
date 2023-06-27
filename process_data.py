from menu import Menu
from cart import Cart
from abc import ABC, abstractmethod

class ProcessData(ABC):

    def __init__(self):
        pass




    @abstractmethod
    def get_cart(menu: Menu):
        
        cart = []

        for section in menu.menu_sections:
            for food_item in section.food_items:
                cart.append(food_item)

        return cart




    @abstractmethod
    def get_total_price(cart: Cart):

        total_price = 0

        for item_cart in cart:
            total_price += item_cart.price

        return total_price