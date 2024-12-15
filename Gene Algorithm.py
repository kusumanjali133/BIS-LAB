import random

# Define the objective function (fitness function)
def fitness_function(x):
    return x ** 2

# Parameters
population_size = 100
mutation_rate = 0.1
crossover_rate = 0.7
num_generations = 2
x_range = (-10, 10)

# Initialize population
population = [random.uniform(x_range[0], x_range[1]) for _ in range(population_size)]

# Genetic Algorithm
for generation in range(num_generations):
    # Evaluate fitness
    fitness = [fitness_function(x) for x in population]

    # Track the best solution
    best_x = max(population, key=fitness_function)
    best_fitness = fitness_function(best_x)

    # Create new population
    new_population = []
    while len(new_population) < population_size:
        # Select parents via roulette wheel selection
        total_fitness = sum(fitness)
        selection_probs = [f / total_fitness for f in fitness]
        parent1, parent2 = random.choices(population, weights=selection_probs, k=2)

        # Crossover and mutation
        if random.random() < crossover_rate:
            offspring = (parent1 + parent2) / 2  # Simple averaging crossover
        else:
            offspring = parent1  # No crossover

        # Apply mutation
        if random.random() < mutation_rate:
            offspring = random.uniform(x_range[0], x_range[1])

        new_population.append(offspring)

    population = new_population

# Output the best solution
print(f"Best solution: x = {best_x}, f(x) = {best_fitness}")
