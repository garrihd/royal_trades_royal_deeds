from abc import ABC

class HarmfulSpell(ABC):
    def __init__(self):
        self.damage_type = None
        self.damage: int = 0
        self.duration: int = 0
        