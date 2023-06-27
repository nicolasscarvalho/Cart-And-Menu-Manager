from dataclasses import dataclass
from typing import List
from food import Food

@dataclass
class Cart:

    food_items: List[Food]
