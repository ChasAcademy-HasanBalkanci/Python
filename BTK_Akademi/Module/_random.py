import random
from math import ceil
'''
result = dir (random)
print(result)
result = help(random)
print(result)'''

result = random.random() # random number generator between 0 and 1
result = ceil(random.uniform(10, 23)) # random number generator between 10 and 21
result = random.randint(9, 12)

greeting = 'Hello There'
names = ['ali', 'yagmur', 'deniz', 'cenk', 'ahmet', 'mehmet']

result = names[random.randint(0, len(names) - 1)]
result = random.choice(names)
result = random.choice(greeting)

liste = list(range(10))
new_list = liste[:]

random.shuffle(new_list)

liste = range(100)
first_num = int(input("Enter a first number :"))
last_num = int(input("Enter the last number : ")) 

result = random.sample(liste, random.randint(1,9))
result = random.sample(names, random.randint(first_num, last_num))

print(result)