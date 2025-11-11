from imports import pickle

def save_parameters_to_pkl(q_scores: dict):
    with open('/workspaces/monte-carlo/state_action_average_reward.pkl', 'wb') as f:
            pickle.dump(q_scores, f)