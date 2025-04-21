from abc import ABC, abstractmethod


class Unit(ABC):
    """
    Abstract class to define basic unit behaviour
    """

    def __init__(self, initial_strength: int, training_points: int, training_cost: int):
        self._strength_points = initial_strength
        self._training_points = training_points
        self._training_cost = training_cost

    def __str__(self) -> str:
        return f"Stregth points: {self.strength_points}, training points: {self._training_points}, training cost: {self.training_cost}"

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def training_cost(self) -> int:
        return self._training_cost

    @property
    def strength_points(self) -> int:
        return self._strength_points

    def set_strength_points(self, points: int) -> None:
        self._strength_points = points

    def train(self):
        self._strength_points += self._training_points
