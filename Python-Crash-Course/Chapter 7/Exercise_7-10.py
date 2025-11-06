destination_poll =[]
condition = True
while condition: 
    dream_destination = input("Insert your dream vacation: ")
    destination_poll.append(dream_destination)

    question = input("Press Y if you want to exit or N to continue: ")
    if question.upper() == 'Y':
        condition = False

counting_destination = set(destination_poll)

for i in counting_destination:
    print(f"The {i} was chosen by {destination_poll.count(i)}")