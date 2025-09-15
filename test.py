from imports import pickle

with open('/workspaces/monte-carlo/state_action_average_reward.pkl', 'rb') as f:
    state_action_average_reward = pickle.load(f)

for i, dict in state_action_average_reward.items():
    print(i, dict)