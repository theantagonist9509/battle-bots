# Necessary imports
from GameState import GameState
from Action import Action
from threading import Thread

# For the exmple bot that plays randomly; you probably don't need this line for your own bot though
import random

# This is the Player class
# You will make changes here in order to create a bot which can play the game
class Player(Thread):

    # *args is internally used; do not touch!
    def __init__(self, *args):

        # Declare/initialize your variables here
        self.my_example_variable = 0

        # Internally used code; do not touch these 3 lines!
        Thread.__init__(self)
        self.args = args
        self.action = Action(-1)




    # This method will be called when your bot has to make a move
    def act(self, gamestate):

        # The current board state will be passed to you in gamestate.pieces, which is a list of 9 integers that follow the following schema:
        # 0 -> Square is empty
        # 1 -> Square is O (YOUR BOT'S PIECE)
        # 2 -> Square is X (OPPONENT'S BOT'S PIECE)
    
        # The board squares are indexed row-by-row:
        # _0_|_1_|_2_
        # _3_|_4_|_5_
        #  6 | 7 | 8 
    
        # For example, the board state gamestate.pieces=[2, 0, 2, 0, 1, 0, 0, 0, 1] represents the position:
        # _X_|___|_X_
        # ___|_O_|___
        #    |   | O
    
        # If you wish to place your piece on index i of the list, then do
        #     self.action = Action(i)
        #     return

        # For example, substituting i for 3 for the above action and board position would give the new position:
        # _X_|___|_X_
        # _O_|_O_|___
        #    |   | O

        # IMPORTANT: Either bot (your's or your opponent's) could have to make the first move!

        # An example bot that places its piece randomly on empty squares
        while True:
            i = random.randint(0, 8)

            if (gamestate.pieces[i] == 0):
                self.action = Action(i)
                return
    



    # Internally used code; do not touch these 2 lines!
    def run(self):
        self.act(self.args[0])
