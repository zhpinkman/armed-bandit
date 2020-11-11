import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

from amalearn.environment import UniEnv
from amalearn.reward import UniReward
from amalearn.agent import UniAgent
from amalearn.agent import RandomBanditAgent

number_of_arms = 14
# np.random.seed(7)

agg_results1 = list()
agg_qValues1 = list()
agg_results2 = list()
agg_qValues2 = list()
agg_rewards1 = list()
agg_rewards2 = list()
agg_rewards3 = list()

def plot_qValues(plt, qValues):
    qValues_array = np.array(qValues)
    qValues_means = np.mean(qValues_array, axis=0)
    # for index, value in enumerate(qValues_means):
    #     print('waiting time ' + str(index) + ' : ' + str(value))
    # x = np.linspace(0, number_of_arms, 300)
    # a_BSpline = interpolate.make_interp_spline(np.arange(0, number_of_arms), qValues_means)
    # y = a_BSpline(x)
    plt.plot(qValues_means)
    plt.title('qValues corresponding to every waiting arm')
    plt.xlabel('Waiting time')
    plt.ylabel('qValue')
    plt.grid(axis='y')

def plot_AR(plt, AR):
    ARR_array = np.array(AR)
    ARR_means = np.mean(ARR_array, axis=0)
    max_ARR_means = np.max(ARR_means, axis=0)
    plt.plot(100 * max_ARR_means)
    max_index = []
    for i in ARR_means:
        max_index.append(i[-1])
    plt.legend(['waiting time ' + str(np.argmax(max_index))], loc='lower right')
    plt.title('Average rate of using optimal action')
    plt.xlabel('Trials')
    plt.ylabel('AR')
    plt.grid(axis='y')
    plt.annotate(str(np.round(100*max_ARR_means[-1])) + '%', (len(max_ARR_means), 100*max_ARR_means[-1]))

def plot_single_AR(plt, AR, policy):
    ARR_array = np.array(AR)
    ARR_means = np.mean(ARR_array, axis=0)
    max_ARR_means = np.max(ARR_means, axis=0)
    plt.plot(100 * max_ARR_means, label=(policy))
    max_index = []
    for i in ARR_means:
        max_index.append(i[-1])
    plt.annotate(str(np.round(100*max_ARR_means[-1])) + '%', (len(max_ARR_means), 100*max_ARR_means[-1]))

def calc_regret(rewards, qValues):
    rewards_array = np.array(rewards)
    rewards_array = np.reshape(rewards_array, (100000, 5))
    mean_rewards = np.mean(rewards_array, axis=1)
    mean_qValues = np.mean(qValues, axis=0)
    best_qValue = np.max(mean_qValues)
    regrets = [0]
    for i in range(100000):
        regrets.append(regrets[i] + np.absolute(best_qValue - mean_rewards[i]))
    window_regret = []
    for i in range(100000):
        window_regret.append(np.mean(regrets[max(0, i - 20):i + 1]))
    return window_regret

def plot_single_regret(plt, rewards, qValues, policy):
    regret = calc_regret(rewards, qValues)
    plt.plot(regret, label=policy)

def plot_agg_regrets(plt, agg_rewards1, agg_rewards2, agg_qValues1, agg_qValues2, agg_rewards3):
    plot_single_regret(plt, agg_rewards1, agg_qValues1, 'UCB')
    plot_single_regret(plt, agg_rewards2, agg_qValues2, 'eGreedy')
    plot_single_regret(plt, agg_rewards3, agg_qValues2, 'random-eGreedy')
    plot_single_regret(plt, agg_rewards3, agg_qValues1, 'random-UCB')
    plt.legend()
    plt.title('Regrets corresponded to each policy')
    plt.ylabel('Regret')
    plt.xlabel('Trials')
    plt.grid(axis='y')

def plot_agg_AR(plt, agg_results1, agg_results2):
    plot_single_AR(plt, agg_results1, 'UCB')
    plot_single_AR(plt, agg_results2, 'eGreedy')
    plt.legend()
    plt.title('Average rate of using optimal action')
    plt.xlabel('Trials')
    plt.ylabel('AR')
    plt.grid(axis='y')


def perform_one_epoch(number_of_arms, value, index):
    rewards = [UniReward() for i in range(number_of_arms)]
    env = UniEnv(rewards, 100000, '1')
    agent1 = UniAgent('1', env, 'UCB')
    agent2 = UniAgent('2', env, 'eGreedy')
    agent3 = RandomBanditAgent('3', env)
    agent1.setup()
    agent2.setup()
    results1 = [list() for i in range(number_of_arms)]
    results2 = [list() for i in range(number_of_arms)]
    results3 = [list() for i in range(number_of_arms)]
    for step in range(100000):
        counts1, qValues1, reward1 = agent1.take_action()
        counts2, qValues2, reward2 = agent2.take_action()
        obs, r, d, i = agent3.take_action()
        agg_rewards1.append(reward1)
        agg_rewards2.append(reward2)
        agg_rewards3.append(r)
        for i in range(number_of_arms):
            results1[i].append(counts1[i] / sum(counts1))
            results2[i].append(counts2[i] / sum(counts2))
    return (results1, qValues1), (results2, qValues2) 



for j in range(5):
    print('epoch ' + str(j + 1))
    (results1, qValues1), (results2, qValues2) = perform_one_epoch(number_of_arms, 10, None)
    agg_results1.append(results1)
    agg_qValues1.append(qValues1)
    agg_results2.append(results2)
    agg_qValues2.append(qValues2)

# plt.subplot(221)
# plot_AR(plt, agg_results1)
# plt.subplot(222)
# plot_qValues(plt, agg_qValues1)
# plt.subplot(223)
# plot_AR(plt, agg_results2)
# plt.subplot(224)
# plot_qValues(plt, agg_qValues2)

# plot_agg_regrets(plt, agg_rewards1, agg_rewards2, agg_qValues1, agg_qValues2, agg_rewards3)
plot_agg_AR(plt, agg_results1, agg_results2)

plt.show()



