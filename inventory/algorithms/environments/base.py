from typing import Set, Tuple


class Environment:
    def get_actions(self, state: int) -> Set[int]:
        """
        Should define the actions allowed by the environment.
        """
        pass

    def response(self, state: int, action: int) -> Tuple[int, float]:
        """
        Should define the response of the environment to a
        certain action. Must return the new state and the reward.
        """
        pass
