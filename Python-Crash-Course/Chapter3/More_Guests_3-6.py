guests_list = ['Catalin','Lavinia','Tudor','Ana','Radu']
not_atending = 'Lavinia'
new_guest = 'Andrei'

guests_list.insert(0, 'Lavinia')
guests_list.insert(3, 'Diana')
guests_list.append('Cristi')

print("Only two guests can be invited")

guests_list.pop()

while len(guests_list) > 2:
    guests_list.pop(-1)
print(f'Final Guest list {guests_list[0]} and {guests_list[1]}')