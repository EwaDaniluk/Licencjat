# import ray.rllib.algorithms.ppo
# # https://huggingface.co/trtd56/ppo-CartPole
#
#
# class AgentPPO:
#     def __init__(self, training_iteration, lr, gamma, epsilon, env):
#         self.config = {
#             "env": env,
#             # "framework": "tf",
#             # "lr": lr,
#             "gamma": gamma,
#             # "initial_epsilon": epsilon,
#             # "final_epsilon": 0.01,
#             'torch_deterministic': True,
#             'cuda': True,
#             'track': False,
#             'capture_video': False,
#             'learning_rate': 0.00025,
#             'num_envs': 4,
#             'num_steps': 128,
#             'anneal_lr': True,
#             'gae': True,
#             # 'gamma': 0.99,
#             'gae_lambda': 0.95,
#             'num_minibatches': 4,
#             'update_epochs': 4,
#             'norm_adv': True,
#             'clip_coef': 0.2,
#             'clip_vloss': True,
#             'ent_coef': 0.01,
#             'vf_coef': 0.5,
#             'max_grad_norm': 0.5,
#             'target_kl': None,
#             'minibatch_size': 128,
#             }
#         self.stop = {"training_iteration": training_iteration}
#
#         # Inicjalizacja Ray
#         ray.shutdown()
#         ray.init(
#             num_cpus=3,
#             include_dashboard=False,
#             ignore_reinit_error=True,
#             log_to_driver=False,
#         )
#
#     def train(self, algorithm):
#         # Uruchomienie treningu
#         analysis = ray.tune.run(
#             algorithm,
#             config=self.config,
#             stop=self.stop,
#             checkpoint_at_end=True,
#             checkpoint_freq=1,
#         )
#
#         avg_reward = []
#         for result in analysis.trial_dataframes.values():
#             avg_reward.append(result["episode_reward_mean"])
#
#         return analysis, avg_reward
#
#
import ray.rllib.algorithms.ppo
# https://huggingface.co/trtd56/ppo-CartPole


class AgentPPO:
    def __init__(self, training_iteration, lr, gamma, epsilon, env):
        self.config = {
            "env": env,
            "lr": lr,
            "gamma": gamma,
            "initial_epsilon": epsilon,
            "final_epsilon": 0,
            "framework": "tf",

            }

        # self.stop = {"training_iteration": training_iteration}
        self.stop = {"time_total_s": training_iteration,
                     "sampler_results/episode_reward_mean": 250,
                     }

        # Inicjalizacja Ray
        ray.shutdown()
        ray.init(
            num_cpus=3,
            include_dashboard=False,
            ignore_reinit_error=True,
            log_to_driver=False,
        )

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


