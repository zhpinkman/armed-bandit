import numpy as np
from amalearn.agent import AgentBase

class NetAgent(AgentBase):
    def __init__(self, id, environment, policy):
        super(NetAgent, self).__init__(id, environment)
        self.policy = policy
        self.qValues = list()
        self.counts = list()
        self.observation = list()
        self.eps = .5

    def setup(self):
        actions_n = self.environment.available_actions()
        self.qValues = [100.0 for i in range(actions_n)]
        self.counts = [0 for i in range(actions_n)]
        self.observation = [list() for i in range(actions_n)]


    def pick_arm(self):
        available_actions = self.environment.available_actions()
        p = np.random.random() 
        if p < self.eps:
            chosen_arm_index = np.random.choice(available_actions)
        else:
            chosen_arm_index = np.argmin(self.qValues)
        return chosen_arm_index
        
        
        
    def update_params(self, chosen_arm_index, reward):
        self.counts[chosen_arm_index] += 1
        n = self.counts[chosen_arm_index]
        value = self.qValues[chosen_arm_index]
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.qValues[chosen_arm_index] = new_value


        


    def take_action(self):
        chosen_arm_index = self.pick_arm()
        observation, reward, done, info = self.environment.step(chosen_arm_index)
        self.observation[chosen_arm_index].append(reward)
        self.update_params(chosen_arm_index, reward)
        if sum(self.counts) % 10 == 0:
            self.eps -= 0.0005 
        return self.counts, self.qValues
