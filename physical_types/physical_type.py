from abc import ABC


class PhysicalType(ABC):
    def __init__(self):
        self.dispellable: bool = False