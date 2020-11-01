import numpy as np

from amalearn.environment import MutliArmedBanditEnvironment
from amalearn.reward import UniReward
from amalearn.agent import RandomBanditAgent


rewards = [UniReward() for i in range(14)]
env = MutliArmedBanditEnvironment(rewards, 10, '1')
agent = RandomBanditAgent('1', env)

for step in range(10):
    agent.take_action()