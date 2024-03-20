import ray

from DQN_agent import AgentDQN
from A2C_agent import AgentA2C
from PPO import AgentPPO


class AgentWrapper:
    def __init__(self, training_iteration, lr, gamma, epsilon, env, algorithm):
        self.training_iteration = training_iteration
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.env = env
        self.algorithm = algorithm

    def train_agent(self):
        if self.algorithm == "DQN":
            # agent = AgentDQN(self.training_iteration, self.lr, self.gamma, self.epsilon, self.env)
            # analysis, avg_reward = agent.train(self.algorithm)
            try:
                agent = AgentDQN(self.training_iteration, self.lr, self.gamma, self.epsilon, self.env)
            except Exception as e:
                error_message = ray.get_error_message()
                print("Error creating DQN agent:", error_message)
                # Dodaj dodatkową logikę obsługi błędu lub zidentyfikuj problem
            analysis, avg_reward = agent.train(self.algorithm)
        elif self.algorithm == "A2C":
            agent = AgentA2C(self.training_iteration, self.lr, self.gamma, self.epsilon, self.env)
            analysis, avg_reward = agent.train(self.algorithm)
        else:
            agent = AgentPPO(self.training_iteration, self.lr, self.gamma, self.epsilon, self.env)
            analysis, avg_reward = agent.train(self.algorithm)

        # Zapis wyników do pliku
        with open("wyniki.csv", "w") as f:
            for i, reward in enumerate(avg_reward):
                f.write("{}\t{}\n".format(i, reward))

        return avg_reward
