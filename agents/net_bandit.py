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
    plt.xticks(np.arange(len(means), step=2))
    plt.title('qValues corresponding to every arm which is a path thorough network')
    plt.xlabel('Path index')
    plt.ylabel('qValue')

def plot_AR(plt, AR):
    ARR_array = np.array(AR)
    ARR_means = np.mean(ARR_array, axis=0)
    max_ARR_means = np.max(ARR_means, axis=0)
    max_index = []
    for i in ARR_means:
        max_index.append(i[-1])
    plt.plot(100 * max_ARR_means)
    legend_text = 'path index: ' + str(np.argmax(max_index))
    plt.legend([legend_text])
    plt.title('Average rate of using optimal action with lr = 0.01')
    plt.xlabel('Trials')
    plt.ylabel('AR')
    plt.grid(axis='y')
    plt.annotate(str(np.round(100*max_ARR_means[-1])) + '%', (len(max_ARR_means), 100*max_ARR_means[-1]))

def plot_single_AR(plt, AR):
    ARR_array = np.array(AR)
    ARR_means = np.mean(ARR_array, axis=0)
    max_ARR_means = np.max(ARR_means, axis=0)
    max_index = []
    for i in ARR_means:
        max_index.append(i[-1])
    plt.plot(100 * max_ARR_means)
    legend_text = 'path index: ' + str(np.argmax(max_index))
    plt.annotate(str(np.round(100*max_ARR_means[-1])) + '%', (len(max_ARR_means), 100*max_ARR_means[-1]))
    return legend_text 

def plot_agg_AR(plt, agent1_agg_results, agent2_agg_results):
    legend_text1 = plot_single_AR(plt, agent1_agg_results)
    legend_text2 = plot_single_AR(plt, agent2_agg_results)

    plt.legend(['eGreedy: ' + legend_text1, 'gradient: ' + legend_text2])
    plt.title('Average rate of using optimal action with lr = 0.01')
    plt.xlabel('Trials')
    plt.ylabel('AR')
    plt.grid(axis='y') 


def plot_agg_rewards(plt, agent1_agg_rewards, agent2_agg_rewards):
    rewards1 = np.array(agent1_agg_rewards)
    rewards2 = np.array(agent2_agg_rewards)
    print(rewards1.shape)
    rewards1 = np.reshape(rewards1, (10000, 5))
    rewards2 = np.reshape(rewards2, (10000, 5))
    print(rewards1.shape)
    rewards1_means = np.mean(rewards1, axis=1)
    print(rewards1_means.shape)
    rewards2_means = np.mean(rewards2, axis=1)
    plt.plot(rewards1_means)
    plt.plot(rewards2_means)
    plt.legend(['eGreedy', 'gradient'])
    plt.title('Rewards (delays) observed by each agent')
    plt.ylabel('Delay')
    plt.xlabel('Trials')

c2_list = [1, 2, 3]
c3_list = [4, 5, 6, 7, 8]
c4_list = [9, 10, 11]


rewards = [NetReward(c1, c2, c3) for c1, c2, c3 in itertools.product(c2_list, c3_list, c4_list)]
env = NetEnv(rewards, 10000, '1')
agent = NetAgent('1', env, 'eGreedy')
agent2 = NetAgent('2', env, 'gradient')
agent.setup()
agent2.setup()

agent1_agg_results = []
agent1_agg_qValues = []
agent1_agg_rewards = []
agent2_agg_results = []
agent2_agg_qValues = []
agent2_agg_rewards = []

for i in range(5):
    print('epoch: ', i + 1)
    agent1_results = [list() for i in range(number_of_arms)]
    agent2_results = [list() for i in range(number_of_arms)]
    for step in range(10000):
        agent1_counts, agent1_qValues, agent1_reward = agent.take_action()
        agent2_counts, agent2_qValues, agent2_reward = agent2.take_action()
        agent1_agg_rewards.append(agent1_reward)
        agent2_agg_rewards.append(agent2_reward)
        for i in range(number_of_arms):
            agent1_results[i].append(agent1_counts[i] / sum(agent1_counts))
        for i in range(number_of_arms):
            agent2_results[i].append(agent2_counts[i] / sum(agent2_counts))
    agent1_agg_results.append(agent1_results)
    agent2_agg_results.append(agent2_results)
    agent1_agg_qValues.append(agent1_qValues)
    agent2_agg_qValues.append(agent2_qValues)



# plt.figure()
# plt.subplot(121)
# plot_AR(plt, agent1_agg_results)
# plt.subplot(122)
# plot_AR(plt, agent2_agg_results)
# plot_qValues(plt, agent1_agg_qValues)

plot_agg_AR(plt, agent1_agg_results, agent2_agg_results)
# plot_agg_rewards(plt, agent1_agg_rewards, agent2_agg_rewards)
plt.show()
