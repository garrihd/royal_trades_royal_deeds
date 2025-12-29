from abc import ABC
from magic_types import *

class HelpfulSpell(ABC):
    def __init__(self):
        self.duration: int = 0
        self.mana_cost: int = 0
        self.magic_school: MagicType = None
