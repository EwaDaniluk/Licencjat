import gymnasium
import ray
from ray import tune
from ray.rllib.algorithms.ppo import PPOConfig


class AgentPPO:
    def __init__(self, training_iteration, lr, gamma, epsilon, env, num_workers=2):
        self.config = {
            "env": "CarRacing-v2",
            "num_workers": num_workers,
            "framework": "torch",
            "lambda": 0.95,
            "clip_param": 0.2,
            "kl_coeff": 0.5,
            "num_sgd_iter": 10,
            "lr": 0.0003,
            "sgd_minibatch_size": 128,
            "train_batch_size": 1024,
            "model": {
                "fcnet_hiddens": [256, 256],
            },
        }

        self.stop = {"timesteps_total": 100000}

        ray.init()

    def train(self, algorithm):
        # Uruchomienie treningu
        analysis = ray.tune.run(
            algorithm,
            config=self.config,
            stop=self.stop,
            checkpoint_at_end=True,
            checkpoint_freq=1,
        )

        avg_reward = []
        for result in analysis.trial_dataframes.values():
            avg_reward.append(result["episode_reward_mean"])

        return analysis, avg_reward




# # Inicjalizacja agenta i rozpoczęcie treningu
# agent = CarRacingPPOAgent()
# analysis = agent.train()
