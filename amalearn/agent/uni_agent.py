import numpy as np
from amalearn.agent import AgentBase

class UniAgent(AgentBase):
    def __init__(self, id, environment, policy, mon):
        super(UniAgent, self).__init__(id, environment)
        self.policy = policy
        self.lamda = -2.25
        self.alpha = 0.88
        self.beta = 0.88
        self.monetary_value = 2000.0 / mon
        self.qValues = list()
        self.counts = list()
        self.delay_border = 10
        self.eps = 0.5

    def setup(self):
        actions_n = self.environment.available_actions()
        self.qValues = [8.0 for i in range(actions_n)]
        self.counts = [0 for i in range(actions_n)]


    def pick_arm(self):
        available_actions = self.environment.available_actions()
        p = np.random.random() 
        if p < self.eps:
            chosen_arm_index = np.random.choice(available_actions)
        else:
            chosen_arm_index = np.argmax(self.qValues)
        return chosen_arm_index
        
        
        
    def update_params(self, chosen_arm_index, reward):
        self.counts[chosen_arm_index] += 1
        n = self.counts[chosen_arm_index]
        value = self.qValues[chosen_arm_index]
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.qValues[chosen_arm_index] = new_value
        

    def apply_subjective(self, chosen_arm_index, reward):
        # you get bus
        if reward <= chosen_arm_index:
            if reward <= self.delay_border:
                return (self.delay_border - reward)**self.alpha + self.monetary_value
            else:
                return self.lamda * (reward - self.delay_border)**self.beta + self.monetary_value
        # you get taxi
        else:
            if chosen_arm_index <= self.delay_border:
                return (self.delay_border - chosen_arm_index)**self.alpha
            else:
                return self.lamda * (chosen_arm_index - self.delay_border)**self.beta


        


    def take_action(self):
        chosen_arm_index = self.pick_arm()
        observation, reward, done, info = self.environment.step(chosen_arm_index)
        reward = self.apply_subjective(chosen_arm_index, reward)
        self.update_params(chosen_arm_index, reward)
        self.environment.render()
        # print(self.qValues)
        if sum(self.counts) % 100 == 0:
            # print(self.qValues)
            self.eps -= 0.005 
        # print(self.eps)
        return self.counts