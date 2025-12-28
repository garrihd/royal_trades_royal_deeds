from bolt_spells.bolt_spell import BoltSpell
from harmful_spells.debuff import Debuff

class FireBolt(BoltSpell, Debuff):
    def __init__(self):
        super().__init__()
