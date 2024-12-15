# prompt: particle swarm optimization algorithm give small code

import random

class Particle:
    def __init__(self, dimensions):
        self.position = [random.uniform(-5, 5) for _ in range(dimensions)]
        self.velocity = [random.uniform(-1, 1) for _ in range(dimensions)]
        self.best_position = self.position[:]
        self.best_fitness = float('inf')

def fitness_function(position):
    # Example fitness function (sphere function)
    return sum(x**2 for x in position)


def particle_swarm_optimization(dimensions, num_particles, max_iterations):
    particles = [Particle(dimensions) for _ in range(num_particles)]
    global_best_position = particles[0].position[:]
    global_best_fitness = float('inf')

    for _ in range(max_iterations):
        for particle in particles:
            fitness = fitness_function(particle.position)
            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position[:]

            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = particle.position[:]

            # Update velocity and position
            w = 0.7  # Inertia weight
            c1 = 1.4  # Cognitive coefficient
            c2 = 1.4  # Social coefficient
            r1 = random.random()
            r2 = random.random()
            for i in range(dimensions):
                particle.velocity[i] = w * particle.velocity[i] + \
                    c1 * r1 * (particle.best_position[i] - particle.position[i]) + \
                    c2 * r2 * (global_best_position[i] - particle.position[i])
                particle.position[i] += particle.velocity[i]

    return global_best_position, global_best_fitness

# Example usage
dimensions = 2
num_particles = 30
max_iterations = 100

best_position, best_fitness = particle_swarm_optimization(dimensions, num_particles, max_iterations)

print("Best position:", best_position)
print("Best fitness:", best_fitness)
