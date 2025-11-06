list_of_pizzas = ['salami','quatro stagionni', 'margerita','diavola','hawai']
friend_pizzas = list_of_pizzas[:]

list_of_pizzas.append('quattro formagi')
friend_pizzas.append('special pizza')

for pizza in list_of_pizzas:
    print(f'My favorite pizza is {pizza}')
    
for pizza in friend_pizzas:
    print(f'My friend favorite pizza are {pizza}')