from mage_config.mage_spells.firebolt import FireBolt
from units import Hero, NPC
from units.hero_class import Hero
import asyncio

class Mage(Hero):
    def __init__(self, name: str):
        super().__init__()
        self.intellect = self.intellect + 10
        self._name: str = name
        self.firebolt = FireBolt()
        
    @property
    def name(self):
        return self._name

    async def cast_firebolt(self, target: Hero | NPC) -> None:
        caster = self
        if target == caster:
            print("Invalid target")
            return
        if self.firebolt.is_on_cooldown():
            print("Firebolt on cooldown!")
            return
        dist_to_targ: float = self.get_distance(target)
        print(f"{self.name} begins casting Firebolt...")
        self.firebolt.cast_task = asyncio.create_task(
            self.firebolt.cast_firebolt(target=target,
                                        dist_to_target=dist_to_targ)
        )
        await self.firebolt.cast_task
    
    