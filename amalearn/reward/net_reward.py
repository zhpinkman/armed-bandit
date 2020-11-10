from amalearn.reward import RewardBase
import numpy as np

class NetReward(RewardBase):
    def __init__(self):
        super(NetReward, self).__init__()
        self.link_delays = {
            'b': (2, .2), 
            'g': (0, 6), 
            'o': (5, 6.5)
        }
        self.delay_dict = {
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
        self.p_dict = {
            1: .1, 2: .06, 3: .15, 4: .5, 5: .1, 
            6: .15, 7: .65, 8: .12, 9: .2, 10: .05, 11: .45
        }

    def get_reward(self, c1, c2, c3):
        delay = 0
        for c in [c1, c2, c3]:
            delay += 30 * np.random.binomial(1, self.p_dict[c])
        path = list()
        path.append('0' + str(c1))
        path.append(str(c1) + str(c2))
        path.append(str(c2) + str(c3))
        path.append(str(c3) + '12')
        for link in path:
            delay += self.link_delays[self.delay_dict[link]]
        return get_reward
        
