from src.rl_path_finder.constants import GAMMA

def get_discounted_reward(rewards, Gt_reward=0, discounted_rewards=[]):  
    if not rewards: return discounted_rewards[::-1]
    
    Gt_reward = Gt_reward * GAMMA + rewards[-1]
    
    discounted_rewards.append(Gt_reward)

    return get_discounted_reward(rewards[:-1], Gt_reward, discounted_rewards)