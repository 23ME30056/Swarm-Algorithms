from abc import ABC, abstractmethod


class AbstractSwarmAlgorithm(ABC):

    def __init__(self, optimized_function, number_of_agents):
        super().__init__()

        self.optimized_function = optimized_function
        self.number_of_agents = number_of_agents

    @abstractmethod
    def get_best_global_solution(self):
        return NotImplementedError()

    @abstractmethod
    def step(self):
        return NotImplementedError()

    @abstractmethod
    def get_particles(self):
        return NotImplementedError()