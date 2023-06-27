from dataclasses import dataclass
from typing import List
from food import Food

@dataclass
class Section:

    section_name: str
    food_items: List[Food]
