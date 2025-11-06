sandwich_orders = ['salami','humus','vegan','tomato','tuna']
finished_sandwiches =[]

while sandwich_orders: 
    order_a_sandwhich = sandwich_orders.pop()
    finished_sandwiches.append(order_a_sandwhich)
i=0
while i<len(finished_sandwiches):
    print(f'The {finished_sandwiches[i]} was made')
    i =i+1