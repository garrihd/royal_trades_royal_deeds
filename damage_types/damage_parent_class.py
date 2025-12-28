from abc import ABC

class Damage(ABC):
    def __init__(self):
        self.damage: int = 0
        self.damage_over_time: int = 0
        self.duration: int = 0
