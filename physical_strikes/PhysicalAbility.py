from harmful_spells.debuff import Debuff


class PhysicalAbility(Debuff):
    def __init__(self, spell_school: PhysicalAbility | None = None,
                 duration: int | None = None,
                 cast_time: int | None = None,
                 ) -> None:
        super().__init__(duration, spell_school )
        self.damage_type: PhysicalAbility = spell_school
        self.cast_time = 3
        self.damage: int = 0

    def __str__(self):
        return f'Damage Type: {self.damage_type} - Cast Time: {self.cast_time}s'