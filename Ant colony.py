# prompt: give me a code for ant colony optimization problem

import random
import numpy as np

class AntColonyOptimization:
    def __init__(self, distances, n_ants, n_iterations, decay, alpha=1, beta=1):
        self.distances = distances
        self.pheromone = np.ones(distances.shape) / len(distances)
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        shortest_path = None
        shortest_path_length = float('inf')

        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.update_pheromone(all_paths)
            shortest_path, shortest_path_length = self.get_shortest_path(all_paths, shortest_path, shortest_path_length)

        return shortest_path, shortest_path_length

    def gen_path_dist(self, path):
        total_dist = 0
        for i in range(len(path) - 1):
            total_dist += self.distances[path[i]][path[i + 1]]
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = [start]
        visited = set([start])
        for i in range(len(self.distances) - 1):
            current_node = path[-1]
            next_node = self.pick_move(current_node, visited)
            path.append(next_node)
            visited.add(next_node)
        path.append(0)  # Return to the starting node
        return path

    def pick_move(self, current_node, visited):
        probabilities = []
        unvisited = set(range(len(self.distances))) - visited

        for next_node in unvisited:
            pheromone_val = self.pheromone[current_node][next_node]
            distance_val = 1.0 / self.distances[current_node][next_node]  # Inverse of distance
            probability = (pheromone_val ** self.alpha) * (distance_val ** self.beta)
            probabilities.append(probability)

        total_prob = sum(probabilities)
        if total_prob == 0:  # Handle cases where all probabilities are zero
            return random.choice(list(unvisited))

        probabilities = [p / total_prob for p in probabilities]
        return list(unvisited)[np.random.choice(len(probabilities), p=probabilities)]


    def update_pheromone(self, all_paths):
        self.pheromone *= self.decay
        for path, dist in all_paths:
            for i in range(len(path) - 1):
                self.pheromone[path[i]][path[i+1]] += 1.0 / dist

    def get_shortest_path(self, all_paths, shortest_path, shortest_path_length):
      for path, dist in all_paths:
          if dist < shortest_path_length:
              shortest_path = path
              shortest_path_length = dist
      return shortest_path, shortest_path_length
# Example usage:
distances = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

aco = AntColonyOptimization(distances, n_ants=5000, n_iterations=100, decay=0.5)
shortest_path, path_length = aco.run()

print("Shortest path:", shortest_path)
print("Shortest path length:", path_length)
