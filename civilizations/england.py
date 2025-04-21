from units.pikeman import Pikeman
from units.archer import Archer
from units.knight import Knight
from civilizations.civilization import Civilization
from army.army import ArmyFactory


class England(Civilization):
    def __init__(self) -> None:
        super().__init__()

    def create_army(self):
        factory = ArmyFactory()

        army = (
            factory.add_unit(Pikeman, 10)
            .add_unit(Archer, 10)
            .add_unit(Knight, 10)
            .build()
        )

        self.add_army(army)
