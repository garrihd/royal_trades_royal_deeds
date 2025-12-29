from abc import ABC
from magic_types import *

class HarmfulSpell(ABC):
    def __init__(self):
        self.damage_type = None
        self.damage: int = 0
        self.duration: int = 0
        self.magic_school: MagicType = None
        self.mana_cost: int = 0
        