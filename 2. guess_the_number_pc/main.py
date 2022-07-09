import random


def guess_number(x):
    random_number = random.randrange(0, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print(f"Yay, congrats. You have guessed the number {random_number} correctly.")

guess_number(100)


# todo: rendere un app a premi questo gioco!
