from abc import ABC, abstractmethod
from army.army import Army


class Civilization(ABC):
    """
    Abstract class for civilization.
    Each subclass should define how their army is created
    """

    def __init__(self, armies: set[Army] = set()) -> None:
        self._armies = armies

    def __str__(self):
        return f"This civiliation has {len(self.armies)} armies"

    @property
    def armies(self) -> set[Army]:
        return self._armies

    def add_army(self, army: Army) -> None:
        self._armies.add(army)

    @abstractmethod
    def create_army(self) -> None:
        pass
