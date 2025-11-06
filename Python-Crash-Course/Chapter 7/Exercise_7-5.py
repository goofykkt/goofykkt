while True:
    age = int(input("Insert your age: "))
    if age <= 3: 
        print(f"You are {age} years old, the entrance is free")
    elif age > 3 and age <=12: 
        print(f"You are {age} years old, the ticket is 10$")
    elif age > 12 and age <=99: 
        print(f"You are {age} years old, the ticket is 15$")
    else: 
        print(f"You are to old")
        break