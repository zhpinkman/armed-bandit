import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

from amalearn.environment import NetEnv
from amalearn.reward import NetReward
from amalearn.agent import NetAgent

number_of_arms = 14
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

def plot_AR(plt, AR):
    ARR_array = np.array(AR)
    ARR_means = np.mean(ARR_array, axis=0)
    max_ARR_means = np.max(ARR_means, axis=0)
    plt.plot(100 * max_ARR_means)
    plt.legend([('Waiting time: ' + str(i)) for i in range(0, number_of_arms, 2)])
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








