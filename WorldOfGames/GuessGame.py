import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    while True:
        try:
            print(f"Please enter a number between 1 to {difficulty}")
            guess = int(input())
            if 1 <= guess <= difficulty:
                return guess
            else:
                print("Your guess is out of range, Please try again")
        except ValueError:
            print(f"your guess must be in range of 1-{difficulty}")
            continue


def compare_results(secret_number, guess):
    if secret_number == guess:
        return True
    else:
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return print(compare_results(secret_number, guess))
