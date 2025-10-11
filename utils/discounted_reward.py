import sys

sys.setrecursionlimit(100_000)

def get_discounted_reward(rewards, gamma, Gt_reward=0, discounted_rewards=[]):  
    if not rewards: return discounted_rewards[::-1]
    
    Gt_reward = Gt_reward * gamma + rewards[-1]
    
    discounted_rewards.append(Gt_reward)

    return get_discounted_reward(rewards[:-1], gamma, Gt_reward, discounted_rewards)