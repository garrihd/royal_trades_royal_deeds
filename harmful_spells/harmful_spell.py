from abc import ABC
from typing import TYPE_CHECKING

from magic_types import *
import numpy as np
if TYPE_CHECKING:
    from units import Hero, NPC

class HarmfulSpell(ABC):
    def __init__(self):
        self.damage_type = None
        self.damage: int = 0
        self.duration: int = 0
        self.magic_school: MagicType = None
        self.mana_cost: int = 0



    def get_distance(self,
                     x_location,
                     y_location
                    ) -> float:
        p1 = np.array([self.x_location, self.y_location])
        p2 = np.array([x_location, y_location])
        return float(np.linalg.norm(p2 - p1))
