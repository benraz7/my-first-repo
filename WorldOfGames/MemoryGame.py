import random
import os
import time


def clear_console():
    time.sleep(0.7)
    os.system('cls')


def generate_sequence(difficulty):
    random_num_list = random.sample(range(1, 101), difficulty)
    return random_num_list


def get_list_from_user(difficulty):
    while True:
        try:
            list_from_user = []
            print(
                f"Please enter the {difficulty} numbers you remember from the list shown before in the exact order ("
                f"numbers are in range of 1 to 101)")
            for i in range(difficulty):
                val_from_user = int(input())
                if 1 <= val_from_user <= 101:
                    list_from_user.append(val_from_user)
                else:
                    print("Value is out of range please try again")
            return list_from_user
        except ValueError:
            print(f"your guess must be in range of 1-101")
        continue


def is_list_equal(sequence, list_from_user):
    if sequence == list_from_user:
        return True
    else:
        return False
    pass


def play(difficulty):
    sequence = generate_sequence(difficulty)
    print(sequence)
    clear_console()
    list_from_user = get_list_from_user(difficulty)
    return print(is_list_equal(sequence, list_from_user))
