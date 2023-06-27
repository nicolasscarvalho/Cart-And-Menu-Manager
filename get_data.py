from food import Food
from section import Section
from menu import Menu
from typing import List
from abc import ABC, abstractmethod


class GetData(ABC):

    

    @abstractmethod
    def get_food(img: str, title: str, description: str, price: float):
        return Food(img, title, description, price)
        



    @abstractmethod
    def get_section(section_name: str, food_items: List[Food]):
        return Section(section_name, food_items)




    @abstractmethod
    def get_menu(menu_sections: List[Section]):    
        return Menu(menu_sections)