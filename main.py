import json

from gameloop import GameLoop
from deck import Deck


cnfg_path = 'data/config.json'

with open(cnfg_path, 'r') as file:
    config = json.load(file)

game = GameLoop(config)

game.main_loop()
#game.player_decision()

