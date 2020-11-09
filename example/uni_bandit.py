import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

from amalearn.environment import UniEnv
from amalearn.reward import UniReward
from amalearn.agent import UniAgent

number_of_arms = 20
fig = plt.figure(6)

agg_results = list()
agg_qValues = list()

def plot_qValues(plt, qValues):
    qValues_array = np.array(qValues)
    qValues_means = np.mean(qValues_array, axis=0)
    for index, value in enumerate(qValues_means):
        print('waiting time ' + str(index) + ' : ' + str(value))
    x = np.linspace(0, number_of_arms, 300)
    a_BSpline = interpolate.make_interp_spline(np.arange(0, number_of_arms), qValues_means)
    y = a_BSpline(x)
    plt.plot(x, y)
    plt.title('qValues corresponding to every waiting arm')
    plt.xlabel('Waiting time')
    plt.ylabel('qValue')
    plt.grid(axis='y')
    # plt.annotate(str(qValues_means[0]), 
    #     (0, qValues_means[0]))
    # plt.annotate(str(qValues_means[10]), 
    #     (10, qValues_means[10]))

def plot_AR(plt, AR):
    ARR_array = np.array(AR)
    ARR_means = np.mean(ARR_array, axis=0)
    for i in range(0, number_of_arms, 2):
        plt.plot(ARR_means[i])
    plt.legend([('Waiting time: ' + str(i)) for i in range(0, number_of_arms, 2)])
    plt.title('Average rate of using optimal action')
    plt.xlabel('Trials')
    plt.ylabel('AR')


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



for j in range(10):
    results, qValues = perform_one_epoch(fig, number_of_arms, 10, None)
    agg_results.append(results)
    agg_qValues.append(qValues)

plt.subplot(121)
plot_AR(plt, agg_results)
plt.subplot(122)
plot_qValues(plt, agg_qValues)
plt.show()



