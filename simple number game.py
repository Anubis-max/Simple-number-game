import random
import math

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

lower = get_integer_input("Enter the lower limit: ")
upper = get_integer_input("Enter the upper limit: ")
number = random.randint(lower, upper)
number_of_attempts = 0
chances = round(math.log(upper - lower + 1, 2))

print(f"You have only {chances} chances!")

while True:
    if number_of_attempts >= chances:
        print(f"Better luck next time, the number was {number}!")
        break
    
    answer = get_integer_input("Please enter the number: ")
    number_of_attempts += 1

    if answer > number:
        print("You guessed too high!")
    elif answer < number:
        print("You guessed too low!")
    else:
        print(f"Good job! The number was {answer}!")
        break

