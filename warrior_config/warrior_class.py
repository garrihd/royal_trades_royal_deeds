from mage_config.mage_spells.firebolt import FireBolt
from units import Hero, NPC
import asyncio

from warrior_config.warrior_abilities.crushing_blow import CrushingBlow


class Warrior(Hero):
    def __init__(self, name: str):
        super().__init__()
        self.strength = self.strength + 10
        self._name: str = name
        self.crushing_blow = CrushingBlow()

    @property
    def name(self):
        return self._name

    async def cast_crushing_blow(self, target: Hero | NPC) -> None:
        if self.crushing_blow.is_on_cooldown():
            print("Firebolt on cooldown!")
            return
        print(f"{self.name} begins casting Firebolt...")
        self.crushing_blow.cast_task = asyncio.create_task(
            self.crushing_blow.cast_crushing_blow(target=target)
        )
        await self.crushing_blow.cast_task

