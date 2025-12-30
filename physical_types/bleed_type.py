from harmful_spells.debuff import Debuff
from physical_type import PhysicalType

class Bleed(PhysicalType, Debuff):
    def __init__(self):
        super().__init__()