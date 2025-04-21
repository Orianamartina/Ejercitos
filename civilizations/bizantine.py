from units.pikeman import Pikeman
from units.archer import Archer
from units.knight import Knight
from civilizations.civilization import Civilization
from army.army import ArmyFactory


class Bizantine(Civilization):
    def __init__(self) -> None:
        super().__init__()

    def create_army(self):
        factory = ArmyFactory()

        army = (
            factory.add_unit(Pikeman, 5)
            .add_unit(Archer, 8)
            .add_unit(Knight, 15)
            .build()
        )

        self.add_army(army)
