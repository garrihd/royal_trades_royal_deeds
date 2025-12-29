from abc import ABC
from harmful_spells.debuff import Debuff
from units.hero_class import Hero

class NPC(ABC):
    def __init__(self):
        self.strength: int = 5
        self.intellect: int = 5
        self.spirit: int = 5
        self.agility: int = 5
        self.stamina: int = 5
        self.haste: int = 5
        self.debuff_slots: list[Debuff] = []
        self.buff_slots: list = []
        self.forst_resistance: int = 0
        self.fire_resistance: int = 0
        self.shadow_resistance: int = 0
        self.arcane_resistance: int = 0
        self.nature_resistance: int = 0
        self.x_location: int = 0
        self.y_location: int = 0
        self.level: int = 1
        self.experience: int = 0

    def target_self(self):
        pass

    def target(self, target: Hero | NPC):
        pass