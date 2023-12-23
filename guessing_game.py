import random

def guess_the_number(target):
    c = 10  # Number of chances
    while c > 0:
        guess = int(input("Guess the number: "))
        
        if target > guess:
            print("You guessed a smaller number. Guess a bigger one.")
        elif target < guess:
            print("You guessed a larger number. Guess a smaller one.")
        else:
            print("Congratulations! You guessed the correct number. You are the winner!")
            break  # Exit the loop if the guess is correct
        
        c -= 1
    
    else:
        print(f"Oops! You ran out of chances. The correct number was {target}.")

# Generate a random number between upper_limit and lower limit for the user to guess
print("Set the Upper Limit:  ",end="")

upper_limit=int(input())

print("Enter the number which is lower than upper limit but greater than \'0\'")

print("Set the Lower Limit: ",end="")

lower_limit=int(input())

target_number = random.randint(lower_limit, upper_limit)

# Call the function with the target number
guess_the_number(target_number)
