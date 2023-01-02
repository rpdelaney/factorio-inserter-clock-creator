from fractions import Fraction

from draftsman.blueprintable import Blueprint
from draftsman.constants import Direction
from draftsman.entity import (
    ArithmeticCombinator,
    ConstantCombinator,
    DeciderCombinator,
)

from .constants import TICKRATE


class InserterClock:
    def __init__(self, items_per_second: float, stack_size: int):
        self.items_per_second = items_per_second
        self.stack_size = stack_size

        # Calculate ratios
        self.numerator, self.denominator = (
            Fraction(self.stack_size * TICKRATE / self.items_per_second)
            .limit_denominator(1000)
            .as_integer_ratio()
        )

        self.__blueprint__ = Blueprint()
        self.__blueprint__.label = "Clock"
        self.__blueprint__.description = (
            f"Inserter clock for {self.items_per_second} items / second.\n"
            f"Stack size: {self.stack_size}"
        )

        # Create the bp and link up the combinators
        self.yel = DeciderCombinator(
            id="yel",
            position=[4, 0],
            direction=Direction.EAST,
            control_behavior={
                "decider_conditions": {
                    "first_signal": "signal-C",
                    "comparator": "<=",
                    "constant": self.denominator,
                    "output_signal": "signal-dot",
                    "copy_count_from_input": False,
                },
            },
        )
        self.blu = ArithmeticCombinator(
            id="blu",
            position=[2, 0],
            direction=Direction.EAST,
            control_behavior={
                "arithmetic_conditions": {
                    "first_signal": "signal-C",
                    "operation": "%",
                    "second_constant": self.numerator,
                    "output_signal": "signal-C",
                },
            },
        )
        self.red = ConstantCombinator(
            id="red",
            position=[0, 0],
            direction=Direction.EAST,
            control_behavior={
                "filters": [
                    {
                        "index": 1,
                        "signal": {
                            "name": "signal-C",
                            "type": "virtual",
                        },
                        "count": self.denominator,
                    }
                ]
            },
        )

        # build it up
        self.__blueprint__.entities.append(self.red)
        self.__blueprint__.entities.append(self.blu)
        self.__blueprint__.entities.append(self.yel)

        # wire it up
        self.__blueprint__.add_circuit_connection(
            color="green",
            entity_1="red",
            entity_2="blu",
            side2=1,
        )
        self.__blueprint__.add_circuit_connection(
            color="red",
            entity_1="blu",
            entity_2="blu",
            side1=2,
            side2=1,
        )
        self.__blueprint__.add_circuit_connection(
            color="green",
            entity_1="blu",
            entity_2="yel",
            side1=2,
            side2=1,
        )

    @property
    def items_per_second(self) -> float:
        return self._items_per_second

    @items_per_second.setter
    def items_per_second(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError(f"Value must be a float: {value}")
        if value < 0:
            raise ValueError(f"Value must be greater than zero: {value}")
        self._items_per_second = value

    @property
    def stack_size(self) -> int:
        return self._stack_size

    @stack_size.setter
    def stack_size(self, value: int) -> None:
        if value < 0:
            raise ValueError(f"Value must be greater than zero: {value}")
        if not isinstance(value, int):
            raise ValueError(f"Value must be an int: {value}")
        self._stack_size = value

    def __str__(self) -> str:
        return str(self.__blueprint__.to_string())
