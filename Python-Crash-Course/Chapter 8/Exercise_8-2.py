def book_tile (title_to_print):
    print(title_to_print)

condition = True
while condition:
    usser_input = input("Do you want to print a message Y or N: ")
    if usser_input.upper() == 'Y':
        ask_to_print = input("Enter the message to be printed: ")
        ask_to_print.title()
        book_tile(ask_to_print)
    else:
        condition = False