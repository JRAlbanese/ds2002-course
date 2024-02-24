#!C:/Users/jalba/AppData/Local/Microsoft/WindowsApps/python3

import os


favorite_flavor = input('What is your favorite flavor? ')
os.environ['FAV_FLAVOR'] = favorite_flavor

age = input('What is your age? ')
os.environ['AGE'] = age

is_first_year = input('Are you a first-year student at UVA? ')
os.environ['UVA_FIRST_YEAR'] = is_first_year

pizza_topping = input('What is your favorite pizza topping? ')
os.environ['PIZZA_TOPPING'] = pizza_topping

star_wars = input('Which is the best Star Wars film? ')
os.environ['STAR_WARS'] = star_wars


print("Favorite flavor: " + os.getenv('FAV_FLAVOR'))
print("Age: " + os.getenv('AGE'))
print("First-Year at UVA: " + os.getenv('UVA_FIRST_YEAR'))
print("Favorite Pizza Topping: " + os.getenv('PIZZA_TOPPING'))
print("Best Star Wars Film: " + os.getenv('STAR_WARS'))

