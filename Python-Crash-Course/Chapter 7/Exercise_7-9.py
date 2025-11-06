sandwich_orders = ['salami','pastrami','humus','pastrami','vegan','tomato','pastrami','tuna']
finished_sandwiches =[]

print(f"Deli has run of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders: 
    order_a_sandwhich = sandwich_orders.pop()
    finished_sandwiches.append(order_a_sandwhich)
i=0
while i<len(finished_sandwiches):
    print(f'The {finished_sandwiches[i]} was made')
    i =i+1