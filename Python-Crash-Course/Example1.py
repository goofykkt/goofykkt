def title_name(first_name, last_name, age = None):
    """"Return the name asked from the user formated"""
    full_name = f"{first_name} {last_name}"
    if age:
        full_name = f"{first_name} {last_name} {age}"
    
    return full_name.title()

status = True
while status:
    user_input = input("Press Y to continue or N to exit ")
    if user_input.upper() == 'Y':
        first_name = input("Insert your first name: ")
        last_name = input("Insert your last name: ")
        age = input("Insert your age or leave it empty: ")
        print(title_name(first_name,last_name,age))

    if user_input.upper() == 'N':
        status = False
        print("Program will exit!")
        break