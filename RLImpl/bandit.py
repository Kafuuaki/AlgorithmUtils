import random
import numpy as np


PROBABILITIES = [0.2, 0.3, 0.5, 0.75, 0.6]
NUM_BANDIT = 5

EPS = 0.1

def fixRandom(seed=39):
    np.random.seed(seed=seed)
    random.seed(seed)

class Bandit:
    def __init__(self, bandit_index):
        # self.actual_reward = actual_reward
        
        self.estimate_reward = 0
        self.N = 0
        self.bandit_index = bandit_index
        
    def pull(self) -> int:
        reward: int = 0
        if random.random() < PROBABILITIES[self.bandit_index]:
            reward = 1
        
        self._update(reward)
        
        return reward
    
    def _update(self, reward):
        self.N += 1
        self.bandit_index = self.bandit_index
        self.estimate_reward = ((self.N - 1) * self.estimate_reward + reward) / self.N
        
        
class Game:
    def __init__(self, num_bandit=NUM_BANDIT):
        self.num_bandit = num_bandit
        self.bandit = [Bandit(i) for i in range(num_bandit)]
        self.total_reward = 0
        self.best_band = 0
        self.num_exploit = 0
        self.explore = 0
        
        
    def pull(self, num_iter):
        for _ in range(num_iter):
            if random.random() < EPS:
                # explore
                pull_index: int = random.randint(0, self.num_bandit - 1)
            else:
                # exploit
                pull_index: int = np.argmax([re.estimate_reward for re in self.bandit])
                
            # print(pull_index)
            self.bandit[pull_index].pull()
    
        print([re.estimate_reward for re in self.bandit])
    
    def get_best_arm(self):
        return np.argmax([re.estimate_reward for re in self.bandit])
            
    
if __name__ == "__main__":
    fixRandom()
    g = Game()
    g.pull(1000)
    print(g.get_best_arm() + 1)
    