import numpy as np
import matplotlib.pyplot as plt

from amalearn.environment import UniEnv
from amalearn.reward import UniReward
from amalearn.agent import UniAgent

number_of_arms = 14

# np.random.seed(7)
fig = plt.figure(6)

agg_results = list()



def temp(fig, number_of_arms, value, index):

    rewards = [UniReward() for i in range(number_of_arms)]
    env = UniEnv(rewards, 100000, '1')
    agent = UniAgent('1', env, 'eGreedy')
    agent.setup()
    results = [list() for i in range(14)]




    for step in range(100000):
        counts = agent.take_action()
        for i in range(len(results)):
            results[i].append(counts[i] / sum(counts))

    agg_results.append(results)

    # cm = plt.get_cmap('gist_rainbow')
    # ax = fig.add_subplot(3, 4, index + 1)
    # ax.set_title(str(value))
    # ax.grid(axis='y')
    # ax.set_prop_cycle(color=[cm(1.*i/7) for i in range(7)])
    # for i in range(0, len(results), 2):
    #     ax.plot(results[i])
    # ax.legend([i for i in range(0, len(results), 2)])


for j in range(10):
    temp(fig, number_of_arms, 10, None)


aa = np.array(agg_results)
print(aa.shape)

means = np.mean(aa, axis=0)
print(means.shape)
    
for i in range(0, number_of_arms, 2):
    plt.plot(means[i])


plt.legend([i for i in range(0, number_of_arms, 2)])
plt.show()



