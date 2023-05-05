# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part B: Game Playing Agent
from .board import MatrixBoard
from .random_action import random_action
import numpy as np
from referee.game import \
    PlayerColor, Action, SpawnAction, SpreadAction, HexPos, HexDir
# This is the entry point for your game playing agent. Currently the agent
# simply spawns a token at the centre of the board if playing as RED, and
# spreads a token at the centre of the board if playing as BLUE. This is
# intended to serve as an example of how to use the referee API -- obviously
# this is not a valid strategy for actually playing the game!

class Agent:
    def __init__(self, color: PlayerColor, **referee: dict):
        """
        Initialise the agent.
        """
        self._color = color
        self.board = MatrixBoard(np.zeros([2,7,7], dtype=int), 0, 0, 0)
        

    def action(self, **referee: dict) -> Action:
        """
        Return the next action to take.
        """
        return random_action(self.board, self._color)

    def turn(self, color: PlayerColor, action: Action, **referee: dict):
        """
        Update the agent with the last player's action.
        """
        self.board = self.board.next_board(action, color)