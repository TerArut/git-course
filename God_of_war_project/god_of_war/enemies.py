
from .character import Character

class Draugr(Character):
    def __init__(self, level=2):
        super().__init__("Draugr", 150, 150, 30, level)

class Troll(Character):
     def __init__(self, level=5):
        super().__init__("Troll", 700, 700, 80, level)