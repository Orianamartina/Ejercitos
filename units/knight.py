from units.unit import Unit


class Knight(Unit):
    def __init__(self) -> None:
        Unit.__init__(self, initial_strength=20, training_points=10, training_cost=30)

    @property
    def name(self) -> str:
        return "knight"
