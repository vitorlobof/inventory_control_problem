from typing import Set, Tuple
import numpy as np
from ..environments import Environment


class EpsilonGreedy:
    def __init__(
        self,
        epsilon: float,
        environment: Environment,
        initial_state=0
    ) -> None:
        self.epsilon = epsilon
        self.environment = environment
        self.state = initial_state
        self.states = self.environment.states
        self.actions = self.environment.actions
        self.means = np.zeros((self.states, self.actions), dtype="float64")
        self.count = np.zeros((self.states, self.actions), dtype="int64")

    def __str__(self) -> str:
        return f"Epsilon greedy: eps = {round(self.epsilon, 3)}"

    def __repr__(self) -> str:
        return self.__str__()

    def explore(self, actions: Set[int]) -> int:
        """
        Receives the possible actions and chooses the one with
        the bigger mean.
        """
        means = self.means[self.state].copy()

        for i in range(len(means)):
            if i not in actions:
                means[i] = - np.inf

        return np.argmax(means)

    def exploit(self, actions: Set[int]) -> int:
        """
        Receives the possible states, discarts the one with the
        bigger mean, and chooses one of the remain ones randomly.
        """
        if len(actions) == 1:
            return next(iter(actions))

        actions.remove(self.explore(actions))
        p = np.zeros(self.actions, dtype="float64")

        for action in actions:
            p[action] = 1.0

        p /= np.sum(p)

        return np.random.choice(self.actions, p=p)

    def choose(self) -> int:
        """
        Decides the action that will be taken and returns it.
        """
        get_action = np.random.choice(
            [self.explore, self.exploit],
            p=[self.epsilon, 1 - self.epsilon]
        )
        actions = self.environment.get_actions(self.state)
        action = get_action(actions)
        return action

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
        n = self.count[self.state, action] + 1
        mean = self.means[self.state, action]

        self.count[self.state, action] = n
        self.means[self.state, action] = (
            (1 - 1 / n)*mean + (1 / n)*reward
        )

        self.state = new_state
