counter = 0
while True:
    counter +=1
    age = input("Insert your age or quit to exit: ")
    if int(age) <= 3: 
        print(f"You are {age} years old, the entrance is free")
    elif int(age) > 3 and int (age) <=12: 
        print(f"You are {age} years old, the ticket is 10$")
    elif int(age) > 12: 
        print(f"You are {age} years old, the ticket is 15$")
    elif age == 'quit': 
        print(f"The program will exit")
        break

print(f"The loop was executed for {counter+1} times")