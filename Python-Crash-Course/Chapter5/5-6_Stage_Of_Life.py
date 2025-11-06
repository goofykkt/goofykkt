while True:
    test_value = input("Insert Y to continue or E to exit: ").upper()
    if test_value == 'Y':
        age =int (input("Enter your age: "))
        if age < 2:
            print("You are a baby")
        elif (age in range(2,4)):
            print ("You are a toddler")
        elif (age in range(4,13)):
            print ("You are a kid")
        elif (age in range(13,20)):
            print ("You are a teenager")
        elif (age in range(20,65)):
            print ("You are an ault")
        else:
            print("You are an elder")

    else:
        False
        break