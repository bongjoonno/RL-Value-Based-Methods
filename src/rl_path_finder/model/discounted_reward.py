from src.rl_path_finder.constants import GAMMA

def get_discounted_reward(rewards):
    discounted_rewards = []
    Gt_reward = 0

    for r in reversed(rewards):
        Gt_reward = r + (GAMMA * Gt_reward)
        discounted_rewards.append(Gt_reward)
    
    return discounted_rewards[::-1]