from typing import Tuple
from ..environments import Environment


class AlwaysMax:
    def __init__(
        self,
        environment: Environment,
        initial_state=0
    ) -> None:
        self.environment = environment
        self.state = initial_state
        self.states = self.environment.states
        self.actions = self.environment.actions

    def __str__(self) -> str:
        return "Always max"

    def __repr__(self) -> str:
        return self.__str__()

    def explore(self) -> int:
        return self.choose()

    def choose(self) -> int:
        """
        Decides the action that will be taken and returns it.
        """
        actions = self.environment.get_actions(self.state)
        return max(actions)

    def resolve(self, action: int) -> Tuple[int, float]:
        """
        Receives the action choosen and returns the new state
        and the reward.
        """
        return self.environment.response(self.state, action)

    def update(self, action: int, reward: float, new_state: int):
        """
        Updates the means and the count matrices.
        """
        self.state = new_state
