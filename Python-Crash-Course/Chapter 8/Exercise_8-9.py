# -----------------------------------------------------------
# This program will take a series of short text messages
# Will pass them to the funciton show_messages() 
# The funciton will print each message
# -----------------------------------------------------------

def show_messages(list_of_messages):
    counter = 0; 
    for i in list_of_messages:
        counter = counter+1
        print(f'The {counter} messages is: {i}')
    
    

messages =[]
while True:
    text = input("Insert your message or q to quit: ")
    if text.lower() == 'q':
        break
    messages.append(text)

show_messages(messages) 