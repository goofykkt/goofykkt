username_list = []

while True:
    test_input = input("Enter y to continue or e to exit: ").upper()
    if test_input == 'Y':
        if username_list:
            
            username = input("Enter the username: ")
            for username in username_list:
                if username == 'admin':
                    print(f'Hello {username}, would you like to see a status report?')
                else:
                    print (f'Hello {username} ,thank you for loggin in again')
        else:
            print('No users')
                    
    else:
        False
        break