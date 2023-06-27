from cart import Cart

from get_data import GetData
from process_data import ProcessData
from show_ouput import ShowOutput


class GetRestaurantData():


    def __init__(self):
        super().__init__()



    def get_food_(self):

        
        img: str =          str(input('| Food image source: '))
        title: str =        str(input('| Food title: '))
        description: str =  str(input('| Food description: '))
        price: float =      float(input('| Food price: '))
    

        return GetData.get_food(img=img, title=title, description=description, price=price)
    


    def get_section_(self):


        
        section_name: str = str(input('Section name: '))
        food_items = []

        
        items_quantity: int = int(input('Items quantity: '))
        for i in range (1, items_quantity+1):

            print()
            food = self.get_food_()
            food_items.append(food)
            print()
        
        

        return GetData.get_section(section_name, food_items)
    

    
    def get_menu_(self):


        
        sections_quantity: int = int(input('Section quantity: '))
        menu_sections = []

        for i in range(1, sections_quantity+1):

            print('----------------------------------------------')
            section = self.get_section_()
            menu_sections.append(section)
            print('----------------------------------------------')
        

        return GetData.get_menu(menu_sections)
    


class ProcessRestaurantData():

    def __init__(self):
        super().__init__()
        pass
    

    def get_cart_(self, menu):
        return ProcessData.get_cart(menu)
    

    def get_total_price_(self, cart):
        return ProcessData.get_total_price(cart)
    


class ShowRestaurantData():

    def __init__(self):
        super().__init__()
        pass

    def show_order_(self, cart, total_price):
        return ShowOutput.show_order(cart, total_price)