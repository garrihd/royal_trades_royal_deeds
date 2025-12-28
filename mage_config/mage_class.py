from hero_class import Hero
import asyncio

class Mage(Hero):
    def __init__(self, name: str):
        super().__init__()
        self.intellect = self.intellect + 10
        self._name: str = name
        
    @property
    def name(self):
        return self._name
    
        
    async def cast_firebolt(self, target = None) -> None:
        cast_time = 2
        while cast_time > 0:
            print(
                    f'{self.name} is casting a Firebolt !: {cast_time}'
                )
            await asyncio.sleep(1)
            cast_time -= 1
        
        print(f'{self.name} cast fire bolt!')
    
    