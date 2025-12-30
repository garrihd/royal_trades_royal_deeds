import time
from bolt_spells.bolt_spell import BoltSpell
from harmful_spells.debuff import Debuff
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mage_config.mage_class import Mage
from magic_types import FireMagic
import asyncio
from units import Hero, NPC
import math

class FireBolt(BoltSpell, Debuff):
    def __init__(self):
        super().__init__(spell_school=FireMagic())
        self.cast_task: asyncio.Task | None = None
        ### Spell Damage Config
        self.duration = 3
        self.damage = 10
        self.burn_dot = 9
        self.last_cast_time: float = 0
        ### Spell Cooldown Config
        self.cooldown = 7
        ### Spell Range Config
        self.spell_range: int = 5
        ### Coordinates
        self.x_location = 0
        self.y_location = 0

    def is_on_cooldown(self) -> bool:

        return (time.time() - self.last_cast_time) < self.cooldown

    async def cast_firebolt(self, target: Hero | NPC, dist_to_target) -> None:
        if dist_to_target <= self.spell_range:
            try:
                await asyncio.sleep(self.cast_time)
                if self.get_distance(x_location=target.x_location,
                                     y_location=target.y_location) > self.spell_range:
                    print("Target Out of Range !")
                    return
                target.health -= self.damage
                self.last_cast_time = time.time()  # Start cooldown after cast
                print(f"Firebolt hit! Health: {target.health}")
                await self._apply_burn(target)
                target.debuff_slots.pop()
            except asyncio.CancelledError:
                print("Cast interrupted!")
                raise
        else:
            print("Target out of range!")
            return



    async def _apply_burn(self, target: Hero | NPC):
        burn_debuff: Debuff = Debuff(duration=self.duration,
                                     magic_type=self.magic_type,
                                     debuff_name="Burn")
        target.debuff_slots.append(burn_debuff)
        brun_per_tick = math.floor(self.burn_dot / self.duration)
        f"""
        After casting a firebolt, apply a burn that deals {brun_per_tick}
        Fire Damage for {self.duration} seconds.
        """
        burn_duration = self.duration

        while burn_duration > 0:
            target.health -= brun_per_tick
            print(target.health)
            print(target.debuff_slots)
            await asyncio.sleep(1)
            burn_duration -= 1
        return

    def interrupt(self):
        if self.cast_task:
            self.cast_task.cancel()

