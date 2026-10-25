class BanditProblem:
    def __init__(self, samplers):
        self.samplers = samplers
        self.n = len(samplers)
        self.choice_history = []
        self.reward_history = []
    def pull(self, i):
        assert (1<=i) & (i<=self.n), f"Arm {i} does not exist. #Arm = {self.n}"
        reward = self.samplers[i-1].sample()
        self.choice_history.append(i)
        self.reward_history.append(reward)
        return reward
