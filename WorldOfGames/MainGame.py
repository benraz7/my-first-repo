from Live import load_game, welcome
import MemoryGame
import GuessGame
import CurrencyRouletteGame

welcome("Ben")
games = [MemoryGame.play, GuessGame.play, CurrencyRouletteGame.play]
game_num, game_difficulty = load_game()
play = games[game_num - 1]
play(game_difficulty)
