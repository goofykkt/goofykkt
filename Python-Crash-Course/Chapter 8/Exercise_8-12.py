# -----------------------------------------------------------
# Exercise 8-12 Sandwiches
# -----------------------------------------------------------
def sandwich( *ingredients):
    for item in ingredients:
        print(f"The sandwich contains the following {item}")


sandwich_items=[]

while True:
    question = input("What would you like to add on the sandwich or q to exit: ")
    if question.lower() == 'q':
        break
    sandwich_items.append(question)

sandwich(*sandwich_items)
    




