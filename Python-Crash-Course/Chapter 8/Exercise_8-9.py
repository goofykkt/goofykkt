# -----------------------------------------------------------
# This program will take a series of short text messages
# Now we are emptying a list and sending new messages
# -----------------------------------------------------------

def show_messages(list_of_messages):
    counter = 0; 
    for i in list_of_messages:
        counter = counter+1
        print(f'The {counter} messages is: {i}')
    
def send_meesages(list_of_messages):
    sent_messages=[]
    while list_of_messages:
        message = list_of_messages.pop()
        print (f'The {message} message is moving to sent_messages list')
        sent_messages.append(message)
    print (f'The new list of send messages is sent_messages and it is containing {sent_messages}')
    

messages =[]
while True:
    text = input("Insert your message or q to quit: ")
    if text.lower() == 'q':
        break
    messages.append(text)
show_messages(messages)
send_meesages(messages) 