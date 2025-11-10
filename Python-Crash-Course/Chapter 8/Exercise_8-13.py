# -----------------------------------------------------------
# Exercise 8-13 Users profile
# -----------------------------------------------------------

def build_profile(**arguments):
    for item1, item2 in arguments.items():
        print(f"About me {item1}:{item2}")

description ={}
while True:
    about_me1 = input("What detail would you like to give (or q to exit):  ")
    if about_me1.lower() == 'q':
        break
    about_me2 = input("The detail is  ")
    description[about_me1] = about_me2

build_profile(**description) 