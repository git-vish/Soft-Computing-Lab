"""
NOTE:
    set DNA_SIZE to the number of bits in the binary form of upper bound
"""

import numpy as np
import matplotlib.pyplot as plt

# STEP-1: Defining constants
DNA_SIZE = 6
POP_SIZE = 5
CROSS_RATE = 0.8
MUTATION_RATE = 0.003
GENERATIONS = 30
BOUND = [0, 32]


# STEP-2: defining required functions
def func(x):  # function to minimize
    return x ** 2


def translate_dna(pop):
    return pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * BOUND[1]


def get_fitness(fx):
    return 1 / (1 + fx)


def select(pop, fitness):
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True, p=fitness / fitness.sum())
    return pop[idx]


def crossover(parent, pop):
    if np.random.rand() < CROSS_RATE:
        i_ = np.random.randint(0, POP_SIZE, size=1)
        cross_points = np.random.randint(0, 2, size=DNA_SIZE).astype(np.bool)
        parent[cross_points] = pop[i_, cross_points]
    return parent


def mutate(child):
    for point in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            child[point] = 1 if child[point] == 0 else 0
    return child


# STEP-3: Evolution Process
population = np.random.randint(2, size=(POP_SIZE, DNA_SIZE))
final = []

plt.ion()
x = np.linspace(*BOUND, 200)
plt.plot(x, func(x))
plt.title('Genetic Algorithm Minimizing f(x)=x^2')
plt.xlabel('x')
plt.ylabel('f(x) = x^2')


for _ in range(GENERATIONS):
    f = func(translate_dna(population))

    # plotting
    if 'sca' in globals():
        sca.remove()
    sca = plt.scatter(translate_dna(population), f, s=200, lw=0, c='red', alpha=0.5)
    plt.pause(0.05)

    # GA part (evolution)
    fitness = get_fitness(f)
    print('GENERATION:', _ + 1)
    print('\tx:', population[np.argmax(fitness), :])
    population = select(population, fitness)
    pop_copy = population.copy()
    for parent in population:
        child = crossover(parent, pop_copy)
        child = mutate(child)
        parent[:] = child
        final = parent.copy()

print("\n::::] Result [:::::")
print('x:', final)
print('MINIMUM:', func(translate_dna(final)))

plt.ioff()
plt.show()
