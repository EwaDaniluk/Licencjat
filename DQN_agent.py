import ray.rllib.algorithms.dqn


class AgentDQN:
    def __init__(self, training_iteration, lr, gamma, epsilon, env):
        self.config = {
            "env": env,
            "framework": "tf",
            "lr": lr,
            "gamma": gamma,
            "initial_epsilon": epsilon,
            "final_epsilon": 0,
            "model": {
                "fcnet_hiddens": [32],
                "fcnet_activation": "linear",
            },
        }
        self.stop = {"training_iteration": training_iteration}

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


