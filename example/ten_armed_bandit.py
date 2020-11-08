import numpy as np
import matplotlib.pyplot as plt

from amalearn.environment import TenArmedBanditEnv
from amalearn.reward import StdNormalReward
from amalearn.agent import TenArmedBanditAgent

number_of_arms = 10

# np.random.seed(8)

rewards = [StdNormalReward() for i in range(number_of_arms)]
env = TenArmedBanditEnv(rewards, 1000, '1')
agg_results = list()

for i in range(20):
    results = [list() for i in range(10)]
    agent = TenArmedBanditAgent('1', env)
    agent.setup()
    for step in range(1000):
        counts = agent.take_action()
        for i in range(len(results)):
            results[i].append(counts[i] / sum(counts))
    agg_results.append(results)


AR = np.array(agg_results)
AR = np.mean(AR, axis=0)

print(AR.shape)

rewards_means = [reward.get_info() for reward in rewards]
maximum_AR = AR[np.argmax(rewards_means)]


window_AR = list()
for i in range(len(maximum_AR)):
    window_AR.append(np.mean(maximum_AR[max(0, i - 20):i + 1]))




plt.plot(np.multiply(100, window_AR))
plt.annotate(str(np.round(100*window_AR[-1])) + '%', 
    (1000, window_AR[-1] * 100))
plt.title('AR plot')
plt.ylabel('Average rate of using optimal action')
plt.xlabel('Trials')
plt.grid(axis='y')
plt.show()



