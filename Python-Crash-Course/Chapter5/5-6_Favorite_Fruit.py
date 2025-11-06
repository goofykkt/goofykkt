favorite_fruit = ['apple','bananans','orange']

while True:
    test_input = input("Enter y to continue or e to exit").upper()
    if test_input == 'Y':
        check_fruit = input("Enter your favorite fruit: ")
        if check_fruit in favorite_fruit:
            print (f'You like {favorite_fruit}')
        else:
            print(f'The {favorite_fruit} is not favorite')
    else:
        False
        break