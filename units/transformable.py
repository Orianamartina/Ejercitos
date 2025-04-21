from abc import ABC, abstractmethod


class Transformable(ABC):
    """
    Abstract class to define transformation behaviour
    """

    def __init__(self, transformation_cost: int):
        self._transformation_cost = transformation_cost

    @abstractmethod
    def transform(self):
        pass

    @property
    def transformation_cost(self) -> int:
        return self._transformation_cost
