from typing import Tuple, Set
import numpy as np


class InventoryEnvironment:
    states: int = 3
    actions: int = 3

    probs = np.array([
        [1.00, 0.00, 0.00],
        [0.30, 0.70, 0.00],
        [0.09, 0.30, 0.61],
    ], dtype="float64")

    @classmethod
    def get_actions(cls, state: int) -> Set[int]:
        allowed_actions = np.arange(cls.states - state)
        return set(allowed_actions)

    @classmethod
    def response(cls, state: int, action: int) -> Tuple[int, float]:
        reward: float = 0.0
        mid_state: int = state + action

        new_state: int = np.random.choice(cls.states, p=cls.probs[mid_state])

        reward += cls.delivery(action)
        reward += cls.sale(mid_state - new_state)
        reward += cls.maintance(new_state)

        return new_state, reward

    @classmethod
    def sale(cls, units: int) -> float:
        return 10 * units

    @classmethod
    def maintance(cls, units: int) -> float:
        return - 2 * units

    @classmethod
    def delivery(cls, units: int) -> float:
        if units == 0:
            return 0.0

        return - 5
