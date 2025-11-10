# -----------------------------------------------------------
# Exercise 8-14 Cars
# -----------------------------------------------------------

def make_car (car_brand,brand_model,**arguments):
    print(f"About the {car_brand} {brand_model} we know the following details {arguments}")

description ={}
car_brand = input("Insert the car brand: ")
brand_model = input("Insert the car model: ")

while True:
    about_car_1 = input("Give me a detail about car or q to quit: ")
    if about_car_1.lower() == 'q':
        break
    about_car_2 = input("The detail is:  ")
    description[about_car_1] = about_car_2

make_car(car_brand,brand_model,**description) 