import numpy as np



class NormalSampler:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
    def sample(self):
        return np.random.normal(self.mu,self.sigma)
    @classmethod
    def random_init(cls):
        mu = np.random.uniform(1,6)
        sigma = np.random.uniform(1,10)
        return NormalSampler(mu, sigma)
        

class LoadedDie:
    def __init__(self, p):
        self.p = p
    def sample(self):
        return 1 + np.random.choice(6, p=self.p)
    @classmethod
    def random_init(cls):
        p = np.random.uniform(0,1, size=6)
        p = p/sum(p)
        return LoadedDie(p)