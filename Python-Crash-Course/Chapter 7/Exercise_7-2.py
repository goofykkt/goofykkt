NumberOfPeople = int(input("How many people are in your dinner group? "))

if NumberOfPeople > 8:
    print(f"For {NumberOfPeople} people you will have to wait for a table")
else: 
    print(f"For {NumberOfPeople} people we have an empty table")