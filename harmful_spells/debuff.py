from abc import ABC
from harmful_spells.harmful_spell import HarmfulSpell

class Debuff(ABC, HarmfulSpell):
    def __init__(self):
        super().__init__()
