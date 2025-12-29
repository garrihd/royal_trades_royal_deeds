from .magic_type import MagicType

class ShadowMagic(MagicType):
    def __init__(self):
        self.damage_type = self.__class__

    def __repr__(self):
        return self.__class__.__name__