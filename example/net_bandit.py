import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import itertools

from amalearn.environment import NetEnv
from amalearn.reward import NetReward
from amalearn.agent import NetAgent

number_of_arms = 45

agg_results = list()
agg_qValues = list()

def plot_qValues(plt, qValues):
    means = np.mean(qValues, axis=0)
    plt.plot(means)
    plt.grid()
    plt.xticks(np.arange(len(means)))
    plt.title('qValues corresponding to every arm which is a path thorough network')
    plt.xlabel('Path index')
    plt.ylabel('qValue')

def plot_AR(plt, AR):
    ARR_array = np.array(AR)
    ARR_means = np.mean(ARR_array, axis=0)
    max_ARR_means = np.max(ARR_means, axis=0)
    plt.plot(100 * max_ARR_means)
    plt.title('Average rate of using optimal action')
    plt.xlabel('Trials')
    plt.ylabel('AR')
    plt.grid(axis='y')
    plt.annotate(str(np.round(100*max_ARR_means[-1])) + '%', (len(max_ARR_means), 100*max_ARR_means[-1]))


def perform_one_epoch(fig, number_of_arms, value, index):
    rewards = [UniReward() for i in range(number_of_arms)]
    env = UniEnv(rewards, 100000, '1')
    agent = UniAgent('1', env, 'eGreedy')
    agent.setup()
    results = [list() for i in range(number_of_arms)]
    for step in range(100000):
        counts, qValues = agent.take_action()
        for i in range(number_of_arms):
            results[i].append(counts[i] / sum(counts))
    return results, qValues


c2_list = [1, 2, 3]
c3_list = [4, 5, 6, 7, 8]
c4_list = [9, 10, 11]


rewards = [NetReward(c1, c2, c3) for c1, c2, c3 in itertools.product(c2_list, c3_list, c4_list)]
env = NetEnv(rewards, 10000, '1')
agent = NetAgent('1', env, 'eGreedy')
agent.setup()

agg_results = []
agg_qValues = []

for i in range(20):
    results = [list() for i in range(number_of_arms)]
    for step in range(10000):
        counts, qValues = agent.take_action()
        for i in range(number_of_arms):
            results[i].append(counts[i] / sum(counts))
    agg_results.append(results)
    agg_qValues.append(qValues)




plot_AR(plt, agg_results)
# plot_qValues(plt, agg_qValues)
plt.show()
