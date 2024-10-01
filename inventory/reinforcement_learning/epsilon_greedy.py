import numpy as np


class EpsilonGreedy:
    def __init__(
        self,
        states: int,
        actions: int,
        environment,
        epsilon=0.7,
        initial_state=0
    ) -> None:
        self.state = initial_state
        self.epsilon = epsilon
        self.states = [k for k in range(states)]
        self.actions = [k for k in range(actions)]
        self.means = np.zeros((states, actions), dtype="float64")
        self.count = np.zeros((states, actions), dtype="int64")
        self.environment = np.array(environment, dtype="float64")

    def choose_best(self, allowed_actions=None) -> int:
        if allowed_actions is None:
            return np.argmax(self.means[self.state])

        means = []
        for action in allowed_actions:
            if action not in allowed_actions:
                means.append(-float("inf"))
                continue

            means.append(self.means[self.state, action])

        return np.argmax(means)

    def explore(self, allowed_actions=None) -> int:
        if allowed_actions is None:
            allowed_actions = self.actions

        return np.random.choice(allowed_actions)

    def choose(self, allowed_actions=None) -> int:
        choose_best = np.random.choice(
            [True, False],
            p=[self.epsilon, 1 - self.epsilon]
        )

        if choose_best:
            return self.choose_best(allowed_actions=allowed_actions)

        return self.explore(allowed_actions=allowed_actions)

    def new_state(self, state) -> int:
        return np.random.choice(
            self.states,
            p=self.environment[state]
        )

    def update(self, action, reward):
        n = self.count[self.state, action] + 1
        m = self.means[self.state, action]

        self.count[self.state, action] = n
        self.means[self.state, action] = (1 - 1/n)*m + (1/n)*reward
