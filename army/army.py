from units.unit import Unit


class ArmyFactory:
    """
    Army builder class
    """

    def __init__(self):
        self._units: set[Unit] = set()

    def add_unit(self, unit_class: type[Unit], count: int) -> "ArmyFactory":
        self._units.update(unit_class() for _ in range(count))
        return self

    def build(self) -> "Army":
        return Army(self._units)


class Army:

    def __init__(self, initial_units: set[Unit], gold: int = 1000) -> None:
        self._units: set[Unit] = initial_units
        self._gold: int = gold

    def __str__(self) -> str:
        return f"Army with {len(self._units)} nits, {self._gold} gold, total points: {self.total_points()}"

    @property
    def units(self) -> set[Unit]:
        return self._units

    def total_points(self) -> int:
        return sum(unit.strength_points for unit in self._units)

    @property
    def gold(self) -> int:
        return self._gold

    def add_gold(self, gold: int) -> None:
        self._gold += gold

    def spend_gold(self, gold: int) -> None:
        self._gold -= gold

    def can_afford(self, gold: int) -> bool:
        return self.gold >= gold

    def add_unit(self, unit: Unit) -> None:
        self._units.add(unit)

    def remove_unit(self, unit: Unit) -> None:
        if unit in self.units:
            self._units.remove(unit)
        else:
            raise Exception("The unit does not belong to this army")

    def remove_strongest_units(self, count: int = 1) -> None:
        sorted_units = sorted(
            self._units, key=lambda u: u.strength_points, reverse=True
        )

        units_to_remove = sorted_units[: min(count, len(self._units))]

        for unit in units_to_remove:
            self.remove_unit(unit)

    def train_unit(self, unit: Unit) -> None:
        if not unit in self.units:
            raise Exception("Unit does not belong to this army")

        gold_needed = unit.training_cost

        if not self.can_afford(gold_needed):
            raise Exception("Not enough gold to train the unit")

        self.spend_gold(gold_needed)
        unit.train()

    def transform_unit(self, unit: Unit) -> None:
        if not unit in self.units:
            raise Exception("Unit does not belong to this army")
        gold_needed = unit.transformation_cost
        if not self.can_afford(gold_needed):
            raise Exception("Not enough gold to transform unit")
        self.remove_unit(unit)
        self.spend_gold(gold_needed)
        transformed_unit = unit.transform()
        self.add_unit(transformed_unit)
        print("Unit transformed")

    def loose_battle(self) -> None:
        self.remove_strongest_units(2)

    def win_battle(self) -> None:
        self.add_gold(100)

    def draw_battle(self) -> None:
        self.remove_strongest_units(1)

    def fight(self, army: "Army") -> None:
        if not self._units or not army.units:
            raise Exception("One or both armies have no units to fight")

        opponent_points = army.total_points()
        self_points = self.total_points()

        if self_points > opponent_points:
            self.win_battle()
            army.loose_battle()
            print(f"Victory")
        elif self_points < opponent_points:
            self.loose_battle()
            army.win_battle()
            print("Defeat")
        else:
            self.draw_battle()
            army.draw_battle()
            print("Draw")
