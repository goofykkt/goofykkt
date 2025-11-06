guests_list = ['Catalin','Lavinia','Tudor','Ana','Radu']
not_atending = 'Lavinia'
new_guest = 'Andrei'



for i in range (0, len(guests_list)):
    if guests_list[i] == not_atending:
        guests_list[i] = new_guest
    print(f'{guests_list[i]} you are invited to dinner')