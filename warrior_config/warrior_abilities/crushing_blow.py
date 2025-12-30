import time
from harmful_spells.debuff import Debuff
from typing import TYPE_CHECKING
from physical_strikes.PhysicalAbility import PhysicalAbility
from physical_types.blow_type import Blow

if TYPE_CHECKING:
    from warrior_config.warrior_class import Warrior
import asyncio
from units import Hero, NPC
import math

class CrushingBlow(Blow, Debuff):
    def __init__(self):
        super().__init__()
        self.cast_task: asyncio.Task | None = None
        ### Spell Damage Config
        self.duration = 3
        self.damage = 10
        self.last_cast_time: float = 0
        ### Spell Cooldown Config
        self.cooldown = 2
        ### Coordinates
        self.x_loc = 0
        self.y_loc = 0

    def is_on_cooldown(self) -> bool:
        return (time.time() - self.last_cast_time) < self.cooldown

    async def cast_crushing_blow(self,caster: Hero | NPC, target: Hero | NPC) -> None:
        if target == caster:
            print("Invalid target")
            return
        if self.is_on_cooldown():
            print("Ability on cooldown!")
            return

        try:
            target.health -= self.damage
            self.last_cast_time = time.time()  # Start cooldown after cast
            print(f"Crushing Blow hit {target.name}! Health: {target.health}")
            await self._apply_burn(target)
        except asyncio.CancelledError:
            print("Cast interrupted!")
            raise



    async def _apply_burn(self, target: Hero | NPC):
        burn_debuff: Debuff = Debuff(duration=self.duration,
                                     magic_type=self.magic_type)
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


