import InputData as ipd
import numpy as np

solutions_per_pop = 8
pop_size = (solutions_per_pop, ipd.item_number.shape[0])
print('Population size = {}'.format(pop_size))
initial_population = np.random.randint(2, size = pop_size)
initial_population = initial_population.astype(int)
num_generations = 1000
print('Initial population: \n{}'.format(initial_population))