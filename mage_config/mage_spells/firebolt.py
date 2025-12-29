from bolt_spells.bolt_spell import BoltSpell
from harmful_spells.debuff import Debuff
from magic_types import FireMagic
import asyncio
from units import *
import math

class FireBolt(BoltSpell, Debuff):
    def __init__(self):
        super().__init__(spell_school=FireMagic())
        ### Spell Damage Config
        self.duration = 3
        self.damage = 10
        self.burn_dot = 9
        ### Coordinates
        self.x_loc = 0
        self.y_loc = 0


    async def cast_firebolt(self, target: Hero | NPC):
        pass


    async def apply_burn(self, target: Hero | NPC):
        brun_per_tick = math.floor(self.burn_dot / self.duration)
        f"""
        After casting a firebolt, apply a burn that deals {brun_per_tick}
        Fire Damage for {self.duration} seconds.
        """
        burn_duration = self.duration

        while burn_duration > 0:
            target.health -= brun_per_tick
            await asyncio.sleep(1)
            burn_duration -= 1
