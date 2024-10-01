import numpy as np
import matplotlib.pyplot as plt


class Actions:
    def __init__(self, m):
        self.m = m
        self.mean = 0
        self.N = 0

    def choose(self):
        """
        Choose an option.
        """
        return np.random.randn() + self.m

    def update(self, x):
        """
        Update the action-value estimate.
        """
        self.N += 1
        self.mean = (1 - 1.0 / self.N)*self.mean + 1.0 / self.N * x


def run_experiment(m1, m2, m3, epsilon, N):
    actions = [Actions(m1), Actions(m2), Actions(m3)]

    data = np.empty(N)

    for i in range(N):
        p = np.random.random()

        if p < epsilon:
            j = np.random.choice(3)
        else:
            j = np.argmax([a.mean for a in actions])

        x = actions[j].choose()
        actions[j].update(x)

        data[i] = x

    cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

    plt.plot(cumulative_average)
    plt.plot(np.ones(N)*m1)
    plt.plot(np.ones(N)*m2)
    plt.plot(np.ones(N)*m3)
    plt.xscale('log')
    plt.show()

    for a in actions:
        print(a.mean)

    return cumulative_average
