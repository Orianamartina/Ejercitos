from units.transformable import Transformable
from units.unit import Unit
from units.archer import Archer


class Pikeman(Unit, Transformable):

    def __init__(self) -> None:
        Unit.__init__(
            self,
            initial_strength=5,
            training_points=3,
            training_cost=10,
        )
        Transformable.__init__(self, transformation_cost=30)

    def name(self):
        return "Pikeman"

    def transform(self):
        transformed_unit = Archer()
        if self.strength_points < transformed_unit.strength_points:
            transformed_unit.set_strength_points(self.strength_points)
        return transformed_unit
