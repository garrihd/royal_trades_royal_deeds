from abc import ABC

class Hero(ABC):
    def __init__(self):
        self.strength: int = 5
        self.intellect: int = 5
        self.spirit: int = 5
        self.agility: int = 5
        self.stamina: int = 5
        self.haste: int = 5