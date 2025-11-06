while True:
    test_value = input("Insert Y to continue or E to exit: ").upper()
    if test_value == 'Y':
        test_color = input("Enter Alien color: ")
        if test_color == 'green':
            print ("You earn 5 points")
        else:
            print("You earn 10 points")
    else:
        False
        break