def display_message(sentence_to_print):
    print(sentence_to_print)

condition = True
while condition:
    usser_input = input("Do you want to print a message Y or N: ")
    if usser_input.upper() == 'Y':
        ask_to_print = input("Enter the message to be printed: ")
        display_message(ask_to_print)
    else:
        condition = False