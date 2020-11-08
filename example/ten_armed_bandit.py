import numpy as np
import matplotlib.pyplot as plt

from amalearn.environment import TenArmedBanditEnv
from amalearn.reward import StdNormalReward
from amalearn.agent import TenArmedBanditAgent
from amalearn.agent import RandomBanditAgent

def window_AR(agg_results):
    AR = np.array(agg_results)
    AR = np.mean(AR, axis=0)
    rewards_means = [reward.get_info() for reward in rewards]
    maximum_AR = AR[np.argmax(rewards_means)]
    window_AR = list()
    for i in range(len(maximum_AR)):
        window_AR.append(np.mean(maximum_AR[max(0, i - 20):i + 1]))
    return window_AR

def window_regret(mu, agg_rewards):
    rewards = np.array(agg_rewards)
    best_mean = np.max(mu)
    rewards_means = np.mean(rewards, axis=0)
    regrets = [0]
    for i in range(1000):
        regrets.append(regrets[i] + np.absolute(best_mean - rewards_means[i]))
    window_regret = list()
    for i in range(1000):
        window_regret.append(np.mean(regrets[max(0, i - 20):i + 1]))
    return window_regret
        
def plot_AR(plt, window_AR):
    plt.plot(np.multiply(100, window_AR))
    plt.annotate(str(np.round(100*window_AR[-1])) + '%', 
        (1000, window_AR[-1] * 100))
    plt.title('AR plot')
    plt.ylabel('Average rate of using optimal action')
    plt.xlabel('Trials')

def plot_regrets(plt, regrets):
    plt.plot(regrets)
    plt.title('Regrets plot')
    plt.ylabel('Degree of regret')
    plt.xlabel('Trials')


number_of_arms = 10

# np.random.seed(8)

rewards = [StdNormalReward() for i in range(number_of_arms)]
env = TenArmedBanditEnv(rewards, 1000, '1')
agg_results = list()
agg_rewards = list()
random_agg_rewards = list()

for i in range(20):
    results = [list() for i in range(10)]
    observed_rewards = list()
    random_observed_rewards = list()
    agent = TenArmedBanditAgent('1', env)
    random_agent = RandomBanditAgent('2', env)
    agent.setup()
    for step in range(1000):
        counts, mu, reward = agent.take_action()
        obs, r, d, i = random_agent.take_action()
        observed_rewards.append(reward)
        random_observed_rewards.append(r)
        for i in range(len(results)):
            results[i].append(counts[i] / sum(counts))
    agg_rewards.append(observed_rewards)
    random_agg_rewards.append(random_observed_rewards)
    agg_results.append(results)






window_AR = window_AR(agg_results)
regrets = window_regret(mu, agg_rewards)
random_regrets = window_regret(mu, random_agg_rewards)


# plot_AR(plt, window_AR)
plot_regrets(plt, regrets)
plot_regrets(plt, random_regrets)
plt.grid(axis='y')
plt.show()





