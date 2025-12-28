### ABC obtained from magic_types
from harmful_spells.harmful_spell import HarmfulSpell
from magic_types import *


class Debuff(ABC, HarmfulSpell):
    def __init__(self):
        self.debuff_duration: int = 0
