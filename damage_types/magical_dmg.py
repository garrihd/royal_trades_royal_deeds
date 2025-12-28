from damage_types.damage_parent_class import Damage

class Magical:
    pass

class MagicalDmg(Damage):
    def __init__(self):
        super().__init__()
        self.damage_type = Magical