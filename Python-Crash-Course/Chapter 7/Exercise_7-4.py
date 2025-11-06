pizza_topping =""
list_of_toppings =[]

while pizza_topping != 'quit':
    list_of_toppings.append(pizza_topping)
    pizza_topping = input("Enter the topping that you want to add or quit to exit: ")
    print(f'Your {pizza_topping} will pe added to the pizza')


print(f'Your list of toppings is {list_of_toppings}')