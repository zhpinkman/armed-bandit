import numpy as np
import matplotlib.pyplot as plt

from amalearn.environment import TenArmedBanditEnv
from amalearn.reward import StdNormalReward
from amalearn.agent import TenArmedBanditAgent

number_of_arms = 10
# means = [0.1, 0.1, 0.1, 0.1, 0.9]

rewards = [StdNormalReward() for i in range(number_of_arms)]
env = TenArmedBanditEnv(rewards, 1000, '1')
agent = TenArmedBanditAgent('1', env)
agent.setup()
results = [list() for i in range(10)]
agg_results = list()


for step in range(1000):
    counts = agent.take_action()
    for i in range(len(results)):
        results[i].append(counts[i] / sum(counts))




# for i in range(len(results)):
#     plt.plot(results[i])

rewards_means = [reward.get_info() for reward in rewards]
plt.plot(np.multiply(100, results[rewards_means.index(max(rewards_means))]))

# plt.legend([reward.get_info() for reward in rewards])
plt.annotate(str(results[rewards_means.index(max(rewards_means))][-1]), 
    (1000, results[rewards_means.index(max(rewards_means))][-1] * 100))
plt.grid(axis='y')
plt.show()



