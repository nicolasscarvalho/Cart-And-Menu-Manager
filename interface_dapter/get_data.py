from entities.food import Food
from entities.section import Section
from entities.menu import Menu


class GetData:

    def __init__(self):
        pass



    def get_food(self, img, title, description, price):
        
        img: str =          input('| Food image source: ')
        title: str =        input('| Food title: ')
        description: str =  input('| Food description: ')
        price: float =      input('| Food price: ')

        return Food(img, title, description, price)
        




    def get_section(self):
        
        section_name: str = input('Section name: ')
        items_quantity: int = input('Items quantity: ')


        food_items = []


        for i in range (1, items_quantity+1):

            print()
            food: Food = self.get_food()
            food_items.append(food)
            print()
            


        return Section(section_name, food_items)





    def get_menu(self):
        
        sections_quantity: int = input('Section quantity: ')
        menu_sections = []

        for i in range(1, sections_quantity+1):

            print('----------------------------------------------')
            section: Section = self.get_section()
            menu_sections.append(section)
            print('----------------------------------------------')

        
        return menu_sections(menu_sections)