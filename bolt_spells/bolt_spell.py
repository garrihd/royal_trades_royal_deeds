from harmful_spells.harmful_spell import HarmfulSpell


class BoltSpell(HarmfulSpell):
    def __init__(self):
        super().__init__()
        self.damage_type: str = "Spell"
        self.element: str = ""
        self.cast_time = 3