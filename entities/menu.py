from dataclasses import dataclass
from typing import List
from sections import Sections

@dataclass
class Menu:
    menu_sections: List[Sections]
