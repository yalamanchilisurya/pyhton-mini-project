import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 10
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.")
    
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number}.")
            break
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    
    if attempts == 0:
        print(f"Sorry! You've used all your attempts. The number was {number}.")

guess_number()
