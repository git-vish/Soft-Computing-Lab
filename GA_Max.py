"""
NOTE:
    set DNA_SIZE to the number of bits in the binary form of upper bound
"""

import numpy as np

# STEP-1: Defining constants
DNA_SIZE = 3
POP_SIZE = 10
CROSS_RATE = 0.8
MUTATION_RATE = 0.003
GENERATIONS = 10
BOUND = [0, 5]


# STEP-2: defining required functions
def func(pop):  # function to maximize
    x = pop['x']
    y = pop['y']
    return 4 * x + 3 * y


def generate_population():
    pop = {
        'x': np.random.randint(2, size=(POP_SIZE, DNA_SIZE)),
        'y': np.random.randint(2, size=(POP_SIZE, DNA_SIZE))
    }
    return pop


def translate_dna(pop):  # convert binary DNA to decimal
    x = pop['x']
    y = pop['y']
    return {'x': x.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * BOUND[1],
            'y': y.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * BOUND[1]}


def get_fitness(f):
    return f + 0.001 - np.min(f)


def select(pop, fitness):
    x = pop['x']
    y = pop['y']
    index = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True, p=fitness / fitness.sum())
    return {'x': x[index], 'y': y[index]}


# mating process
def crossover(parent, pop):
    x_p = parent['x']
    y_p = parent['y']
    x = pop['x']
    y = pop['y']
    if np.random.rand() < CROSS_RATE:
        i = np.random.randint(0, POP_SIZE, size=1)  # select another individual from population
        cross_points = np.random.randint(0, 2, size=DNA_SIZE).astype(np.bool)  # choose crossover points
        x_p[cross_points] = x[i, cross_points]  # mating and produce one child
        y_p[cross_points] = y[i, cross_points]
    return {'x': x_p, 'y': y_p}


def mutate(child):
    x = child['x']
    y = child['y']
    for point in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            x[point] = 1 if x[point] == 0 else 0
            y[point] = 1 if y[point] == 0 else 0
    return {'x': x, 'y': y}


# STEP-3: Evolution Process
# generating random population
population = generate_population()
final = {}

for _ in range(GENERATIONS):
    f = func(translate_dna(population))

    fitness = get_fitness(f)
    print("GENERATION:", _ + 1)
    print('\tx:', population['x'][np.argmax(fitness), :])
    print('\ty:', population['y'][np.argmax(fitness), :])
    population = select(population, fitness)
    pop_copy = population.copy()

    for i in range(POP_SIZE):
        parent = {
            'x': population['x'][i],
            'y': population['y'][i]
        }
        child = crossover(parent, pop_copy)
        child = mutate(child)
        parent = {
            'x': child['x'],
            'y': child['y']
        }
        final = parent.copy()


print("\n::::] Result [:::::")
print('x:', final['x'])
print('y:', final['y'])
print('MAXIMUM:', func(translate_dna(final)))
