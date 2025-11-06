current_users = ['Tudor','Radu','Ana','Cristi','Dani']
new_users = ['TudoR','Alin','Paul','CRISti','Luci']

def lower_case(lower_item=[]):
    new_lower_item = []
    for i in range (0,len(lower_item)):
        new_lower_item.append(lower_item[i].lower())
    return new_lower_item


while True:
    test_input = input("Enter y to continue or e to exit: ").upper()
    if test_input == 'Y':
        for user_check in new_users:
            if user_check.lower() in lower_case(current_users):
                print (f'Insert a new user, beacause user {user_check.title} already exists ')
            else:
                print(f'User {user_check.title} is available')
                    
    else:
        False
        break