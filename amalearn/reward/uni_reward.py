from amalearn.reward import RewardBase
import numpy as np

class UniReward(RewardBase):
    def __init__(self):
        super(UniReward, self).__init__()
        self.mean = 6
        self.std = 4

    def get_reward(self):
        return np.random.normal(loc=self.mean, scale=self.std)

    def get_info(self):
        return self.mean