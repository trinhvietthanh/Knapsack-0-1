import numpy as np
import pandas as pd
from random import randint
from knapsack import Knapsack
from initial_population import initial_population, num_generations, pop_size
from InputData import weight, value, knapsack_threshold, item_number
import matplotlib.pyplot as plt


def optimize(weight, value, population, pop_size, num_generations, threshold, mutation_rate, crossover_rate):
      parameters, fitness_history = [], []
      num_parents = int(pop_size[0]/2)
      num_offsprings = pop_size[0] - num_parents
      for i in range(num_generations):
          fitness = Knapsack.cal_fitness(weight, value, population, threshold)
          fitness_history.append(fitness)
          parents = Knapsack.selection(fitness, num_parents, population)
          offsprings = Knapsack.crossover(parents, num_offsprings, crossover_rate)
          mutants = Knapsack.mutation(offsprings, mutation_rate)
          population[0:parents.shape[0], :] = parents
          population[parents.shape[0]:, :] = mutants
      print('Last generation: \n{}\n'.format(population))
      fitness_last_gen = Knapsack.cal_fitness(
      weight, value, population, threshold)
      print('Fitness of the last generation: \n{}\n'.format(fitness_last_gen))
      max_fitness = np.where(
          fitness_last_gen == np.max(fitness_last_gen))
      parameters.append(population[max_fitness[0][0], :])
      return parameters, fitness_history

crossover_rate = float(input("Crossover Rate: "))
mutation_rate = float(input("Mutation Rate: "))

parameters, fitness_history = optimize(weight, value, initial_population, pop_size, num_generations, knapsack_threshold, mutation_rate, crossover_rate)
print('Ket qua toi uu: \n{}'.format(parameters))
selected_items = item_number * parameters
print('\nCac vat pham se lua chon:')
for i in range(selected_items.shape[1]):
  if selected_items[0][i] != 0:
     print('{}\n'.format(selected_items[0][i]))


fitness_history_mean = [np.mean(fitness) for fitness in fitness_history]
fitness_history_max = [np.max(fitness) for fitness in fitness_history]
plt.plot(list(range(num_generations)), fitness_history_mean, label = 'Mean Fitness')
plt.plot(list(range(num_generations)), fitness_history_max, label = 'Max Fitness')
plt.legend()
plt.title('Fitness through the generations')
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.show()
print(np.asarray(fitness_history).shape)