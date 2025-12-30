from abc import ABC
from harmful_spells.debuff import Debuff
from typing import TYPE_CHECKING
import numpy as np
if TYPE_CHECKING:
    from units import Hero, NPC


class Hero(ABC):
    def __init__(self):
        self.health: int = 0
        self.mana: int = 0
        self.strength: int = 5
        self.intellect: int = 5
        self.spirit: int = 5
        self.agility: int = 5
        self.stamina: int = 5
        self.haste: int = 5
        self.debuff_slots: list[Debuff] = []
        self.buff_slots: list = []
        self.frost_resistance: int = 0
        self.fire_resistance: int = 0
        self.shadow_resistance: int = 0
        self.arcane_resistance: int = 0
        self.nature_resistance: int = 0
        self.x_location: int = 0
        self.y_location: int = 0
        self.level: int = 1
        self.experience: int = 0

    def target(self, target: Hero | NPC):
        pass

    def get_distance(self, target: Hero | NPC) -> float:
        p1 = np.array([self.x_location, self.y_location])
        p2 = np.array([target.x_location, target.y_location])
        return float(np.linalg.norm(p2 - p1))
