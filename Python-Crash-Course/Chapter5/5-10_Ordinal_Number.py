ordinal_numbers = [1,2,3,4,5,6,7,8,9,10]


while True:
    test_input = input("Enter y to continue or e to exit: ").upper()
    if test_input == 'Y':
        for i in range (1,10):
            if i == 1:
                print (f'\n{i}st\n')
            elif i == 2:
                print (f'{i}nd\n')
            elif i == 3:
                print (f'{i}rd\n')
            else:
                print (f'{i}th\n')
                    
    else:
        False
        break