from harmful_spells.debuff import Debuff
from magic_types import MagicType


class BoltSpell(Debuff):
    def __init__(self, spell_school: MagicType):
        super().__init__()
        self.damage_type: MagicType = spell_school
        self.element: str = ""
        self.cast_time = 3
        self.damage: int = 0

    def __str__(self):
        return f'Damage Type: {self.damage_type} - Cast Time: {self.cast_time}s'

