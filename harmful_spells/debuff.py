from harmful_spells.harmful_spell import HarmfulSpell
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from magic_types import MagicType


class Debuff(HarmfulSpell):
    def __init__(self, duration: int | None = None,
                 magic_type: MagicType | None = None,
                 debuff_name: str | None = None,):
        super().__init__()
        self.duration = duration
        self.magic_type = magic_type
        self.debuff_name = debuff_name

    def __repr__(self):
        return f"{self.debuff_name} {self.__class__.__name__}"
