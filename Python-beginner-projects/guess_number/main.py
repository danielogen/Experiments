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

# guess(10)

"""The computer will try to guess our secret number"""

def computer_guess(x, number):
    print(f"Your secret number is {number}. I will now try to guess it")
    low = 1
    high = x

    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low == high

        feedback = input(f"Is {guess} too low [H] or too high [H], Or correct [C]: ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay! I guessed your secret number correctly")
            
            
computer_guess(1000, 300)