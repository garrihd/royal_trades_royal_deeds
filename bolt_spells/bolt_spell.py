from harmful_spells.debuff import Debuff
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from magic_types import MagicType


class BoltSpell(Debuff):
    def __init__(self, spell_school: MagicType | None = None,
                 duration: int | None = None,
                 magic_type : MagicType | None = None
                 ) -> None:
        super().__init__(duration, magic_type )
        self.damage_type: MagicType = spell_school
        self.element: str = ""
        self.cast_time = 3
        self.damage: int = 0

    def __str__(self):
        return f'Damage Type: {self.damage_type} - Cast Time: {self.cast_time}s'

