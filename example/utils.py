from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

mean = 6
std = 4

beta = 1.5
alpha = .88
lamda = -5
monetary_value = 9
delay_border = 10
h = 1.5

def mean_reward(limit, mode = 0):
    a = np.random.normal(mean, std, 100000)
    b = list()
    for value in a:
        if mode == 0:
            if value < limit:
                b.append(value)
        else:
            if value > limit:
                b.append(value)
    return np.mean(b)

def calc_rewards(chosen_arm):
    result = 0
    p = 0
    if chosen_arm > delay_border:
        p = (chosen_arm - delay_border)**h
    result += stats.norm.cdf(chosen_arm, mean, std) * ( stats.norm.cdf(10, mean, std) * ((delay_border - mean_reward(delay_border))**alpha + monetary_value) + 
        (1 - stats.norm.cdf(10, mean, std)) * (lamda*(mean_reward(delay_border, mode=1) - delay_border)**beta + monetary_value - p) )
    if chosen_arm <= delay_border:
        result += (1 - stats.norm.cdf(chosen_arm, mean, std)) * (delay_border - chosen_arm)**alpha
    else:
        result += (1 - stats.norm.cdf(chosen_arm, mean, std)) * lamda*(chosen_arm - delay_border)**beta
    return result


actual_rewards = list()

for i in range(20):
    actual_rewards.append(calc_rewards(i))

plt.plot(actual_rewards)
plt.show()
