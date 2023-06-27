from cart import Cart
from abc import ABC, abstractmethod

class ShowOutput(ABC):

    def __init__(self):
        super().__init__()
        pass

    
    @abstractmethod
    def show_order(cart: Cart, total_price: float):
        
        for item_cart in cart:
            print(f'{item_cart.title} ------- {item_cart.price}')

        print('----------------------------------------------')

        print(f'Total price: {total_price}')