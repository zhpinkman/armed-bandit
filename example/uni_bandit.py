import numpy as np
import matplotlib.pyplot as plt

from amalearn.environment import UniEnv
from amalearn.reward import UniReward
from amalearn.agent import UniAgent

number_of_arms = 14

# np.random.seed(7)
fig = plt.figure(6)

agg_results = dict()
for i in range(number_of_arms):
    agg_results[i] = list()


def temp(fig, number_of_arms, value, index):

    rewards = [UniReward() for i in range(number_of_arms)]
    env = UniEnv(rewards, 10000, '1')
    agent = UniAgent('1', env, 'eGreedy', value)
    agent.setup()
    results = [list() for i in range(14)]




    for step in range(10000):
        counts = agent.take_action()
        for i in range(len(results)):
            results[i].append(counts[i] / sum(counts))



    cm = plt.get_cmap('gist_rainbow')
    ax = fig.add_subplot(3, 4, index + 1)
    # ax.set_title(str(value))
    ax.grid(axis='y')
    ax.set_prop_cycle(color=[cm(1.*i/7) for i in range(7)])
    for i in range(0, len(results), 2):
        ax.plot(results[i])
    # ax.legend([i for i in range(0, len(results), 2)])



for i, value in enumerate([200, 220, 240, 260, 280, 300, 320, 360, 380, 400, 420, 480]):
    temp(fig, number_of_arms, value, i)


plt.legend([i for i in range(0, number_of_arms, 2)])
plt.show()



