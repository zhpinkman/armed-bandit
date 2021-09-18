import numpy as np
import itertools
import matplotlib.pyplot as plt

link_delays = {
            'b': (2, .2), 
            'g': (0, 6), 
            'o': (5, 6.5)
        }
delay_dict = {
    '01': 'b', '02': 'g', '03': 'o', 
    '14': 'g', '15': 'g', '16': 'g', '17': 'o', '18': 'o',
    '24': 'b', '25': 'o', '26': 'b', '27': 'o', '28': 'b', 
    '34': 'b', '35': 'b', '36': 'b', '37': 'g', '38': 'g', 
    '49': 'g', '410': 'b', '411': 'o', 
    '59': 'o', '510': 'b', '511': 'g', 
    '69': 'b', '610': 'g', '611': 'o', 
    '79': 'o', '710': 'g', '711': 'g', 
    '89': 'g', '810': 'o', '811': 'o', 
    '912': 'b', '1012': 'o', '1112': 'b'
    }
p_dict = {
    1: .1, 2: .06, 3: .15, 4: .5, 5: .1, 
    6: .15, 7: .65, 8: .12, 9: .2, 10: .05, 11: .45
}

c2_list = [1, 2, 3]
c3_list = [4, 5, 6, 7, 8]
c4_list = [9, 10, 11]

paths = [
    (c1, c2, c3)
        for c1, c2, c3 in itertools.product(c2_list, c3_list, c4_list)
]

rewards = []

for path in paths:
    delay = 0
    for c in path:
        delay += 30 * p_dict[c]
    links = list()
    links.append('0' + str(path[0]))
    links.append(str(path[0]) + str(path[1]))
    links.append(str(path[1]) + str(path[2]))
    links.append(str(path[2]) + '12')
    for link in links:
        mean, std = link_delays[delay_dict[link]]
        delay += mean
    rewards.append(delay)


print(paths[22], paths[27])

plt.plot(rewards)
plt.grid()
plt.xticks(np.arange(len(rewards)))
plt.title('Delays corresponding to every arm which is a path through network')
plt.xlabel('path index')
plt.ylabel('Delay')
plt.show()