from application.ma_bandit.samplers import *
from application.ma_bandit.problem import *

N = 5
TURNS = 20
DIST = "LoadedDie"

def generate_problem(n, dist):
    if dist == "Normal":
        sampler = NormalSampler
    elif dist == "LoadedDie":
        sampler = LoadedDie
    else:
        raise NotImplementedError
    samplers = [sampler.random_init() for _ in range(n)]
    return BanditProblem(samplers)

if __name__ == "__main__":
    problem = generate_problem(n = N, dist=DIST)
    t = 0
    while t<TURNS:
        t += 1
        choice = input(f"Turn {t}/{TURNS} | Choose arm (1-{N}): ").strip()
        reward = problem.pull(int(choice))
        print(f"Reward: {reward}\n")
    print("Game over!\n")
    print(f"Choice history: {problem.choice_history}")
    print(f"Reward history: {problem.reward_history}")
    print(f"Total reward: {sum(problem.reward_history)}")
