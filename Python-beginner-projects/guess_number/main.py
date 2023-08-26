import random

def guess(x):
    random_number = random.randint(1, x)

    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > random_number:
            print('Sorry, your guess is too high')
        elif guess < random_number:
            print('Oops!!, your guess is too low')
    print(f"Wow!! congrats!, you have guessed the random number {random_number}")

guess(10)