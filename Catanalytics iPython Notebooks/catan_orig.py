import random

rolls = 5
#raw_input("watcha want")
basket = [1,0,0,0,0]
#raw_input("How many of ('wood', 'wheat', 'brick', 'ore', 'sheep')?")

resources = ['wood', 'wheat', 'brick', 'ore', 'sheep']
numberResources = len(resources)

production = [[2, 2], [4, 6], [1, 11], [], [12]]
histograms = [[0 for i in range(10*int(rolls))] for j in range(numberResources)]
#resources = {'wood': [2, 2], 'wheat': [4,6], 'brick': [1,11], 'ore': [], 'sheep': [12]}

iteration = 10000

def checker(list, item):
  count = 0
  for i in list:
    if i == item:
      count += 1
  return count

def basket_checker(goal, obtained):
  for i in range(numberResources):
    if (obtained[i] < goal[i]):
      return 0
  return 1

def sim(rolls, resources, iteration):
  die_sum = 0
  basket_count = 0 
  for k in range(iteration):
    numObtained = [0 for i in range(numberResources)]
      
    for i in range(rolls):
      die_sum = random.randint(1,6) + random.randint(1,6)
      for index in range(numberResources):
        numObtained[index] += checker(production[index], die_sum)
    
    for index in range(numberResources):
      histograms[index][numObtained[index]] += 1
    
    basket_count += basket_checker(basket, numObtained)
        
  return histograms, basket_count
  
print sim(rolls, resources, iteration)