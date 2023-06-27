from dataclasses import dataclass
from typing import List
from section import Section

@dataclass
class Menu:
    menu_sections: List[Section]
