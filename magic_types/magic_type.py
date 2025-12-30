from abc import ABC


class MagicType(ABC):
    def __init__(self):
        self.dispellable: bool = True