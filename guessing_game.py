import random

def guess_the_number(lower_limit, upper_limit):
    target_number = random.randint(lower_limit, upper_limit)
    chances = 10
    
    while chances > 0:
        guess = int(input("Guess the number: "))
        
        if target_number == guess:
            print("Congratulations! You guessed the correct number.")
            break
        elif target_number > guess:
            print("You guessed too low.")
        else:
            print("You guessed too high.")
        
        chances -= 1
    
    else:
        print(f"Oops! You ran out of chances. The correct number was {target_number}.")

# Input upper and lower limits
upper_limit = int(input("Set the Upper Limit: "))
lower_limit = int(input(f"Set the Lower Limit (must be less than {upper_limit}): "))

# Call the function with the specified limits
guess_the_number(lower_limit, upper_limit)
