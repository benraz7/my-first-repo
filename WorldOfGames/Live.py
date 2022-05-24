def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play.")


def load_game():
    while True:
        try:
            print("Please choose a game to play:")
            print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
            print("2. Guess Game - guess a number and see if you chose like the computer")
            print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
            game_input_from_user = int(input())
            if 1 <= game_input_from_user <= 3:
                while True:
                    try:
                        print(f"Please choose game difficulty from 1 to 5:")
                        difficulty_input_from_user = int(input())
                        if 1 <= difficulty_input_from_user <= 5:
                            return game_input_from_user, difficulty_input_from_user
                        else:
                            print("Game difficulty must be in range of 1-5")
                    except ValueError:
                        print("Game difficulty must be in range of 1-5")
                        continue
                break
            else:
                print("Game option must be in range of 1-3")
        except ValueError:
            print("Game option must be in range of 1-3")
            continue
