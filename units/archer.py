from units.transformable import Transformable
from units.unit import Unit
from units.knight import Knight


class Archer(Unit, Transformable):

    def __init__(self) -> None:
        Unit.__init__(self, initial_strength=10, training_points=7, training_cost=20)
        Transformable.__init__(self, transformation_cost=40)

    @property
    def name(self) -> str:
        return "Archer"

    def transform(self):
        transformed_unit = Knight()
        if self.strength_points < transformed_unit.strength_points:
            transformed_unit.set_strength_points(self.strength_points)
        else:
            transformed_unit.set_strength_points(
                self.strength_points
                - round(self.strength_points - transformed_unit.strength_points / 3)
            )
        return transformed_unit
