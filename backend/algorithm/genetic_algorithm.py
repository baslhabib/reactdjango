import random

# Define the target string
TARGET = "HELLO"

# Function to generate a random string of the same length as TARGET
def random_string(length):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ ') for _ in range(length))

# Function to calculate fitness (number of matching characters)
def fitness(candidate):
    return sum(1 for expected, actual in zip(TARGET, candidate) if expected == actual)

# Function to mutate a string
def mutate(string):
    index = random.randint(0, len(string) - 1)
    char = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
    return string[:index] + char + string[index + 1:]

# Main genetic algorithm function
def run_genetic_algorithm():
    population_size = 100
    generations = 1000

    # Create initial population
    population = [random_string(len(TARGET)) for _ in range(population_size)]

    for _ in range(generations):
        # Sort population by fitness
        population.sort(key=fitness, reverse=True)
        
        # Select the best half to breed
        survivors = population[:population_size // 2]

        # Create a new population
        population = survivors[:]

        # Mutate the survivors to create new individuals
        while len(population) < population_size:
            parent = random.choice(survivors)
            child = mutate(parent)
            population.append(child)

    # Return the best candidate after all generations
    return max(population, key=fitness)
