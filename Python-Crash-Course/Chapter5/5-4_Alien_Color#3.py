while True:
    test_value = input("Insert Y to continue or E to exit: ").upper()
    if test_value == 'Y':
        test_color = input("Enter Alien color: ")
        if test_color == 'green':
            print ("You earn 5 points")
        elif test_color =='yellow':
            print ("You earn 10 points")
        elif test_color == 'red':
            print("You earn 15 points")
        else:
            print("No valid color. You earn 0 points")
    else:
        False
        break