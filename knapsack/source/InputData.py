import numpy as np
import random as rd
from random import randint


number_item = 10
min_weight = 1
max_weight = 15
min_value = 10
max_value = 750
knapsack_threshold = 35    #Can nang cua cai tui
crossover_rate = 0.10
mutation_rate = 0.01

item_number = np.arange(1,number_item + 1)
weight = np.random.randint(min_weight, max_weight, size = number_item)
value = np.random.randint(min_value, max_value, size = number_item)

print('Danh sach vat pham:')
print('ID   Weight  Value')
for i in range(item_number.shape[0]):
    print('{0}          {1}         {2}\n'.format(item_number[i], weight[i], value[i]))