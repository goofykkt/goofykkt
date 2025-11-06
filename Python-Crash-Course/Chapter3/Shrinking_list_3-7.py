guests_list = ['Catalin','Lavinia','Tudor','Ana','Radu']
not_atending = 'Lavinia'
new_guest = 'Andrei'

guests_list.insert(0, 'Lavinia')
guests_list.insert(3, 'Diana')
guests_list.append('Cristi')

print("Only two guests can be invited")

def remove_from_list(list_to_remove, final_size):
    while(len(list_to_remove)>final_size):
        list_to_remove.remove(list_to_remove[-1])
    return list_to_remove


print(f'Final Guest list {remove_from_list(guests_list,2)}')