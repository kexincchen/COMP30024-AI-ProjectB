from alpha_beta.board import MatrixBoard
from referee.game import \
    PlayerColor, Action, SpawnAction, SpreadAction, HexPos, HexDir
import random
class ABNode:
    def __init__(self, board: MatrixBoard, color: PlayerColor):
        self.board = MatrixBoard(board.state, board.turn_count, board.red_power, board.blue_power)
        self.children = []
        self.color = color
        self.action = None
        
    def add_children(self):
        for action in self.board.get_valid_actions(self.color):
            child_board= self.board.next_board(action, self.color)
            child = ABNode(child_board, PlayerColor.RED if self.color == PlayerColor.BLUE else PlayerColor.BLUE)
            child.action = action
            self.children.append(child)

def alpha_beta(node: ABNode, depth: int, alpha, beta, maximize:bool, color: PlayerColor):
    if (depth==0) or (node.board.game_over()):
        return eval(node.board, PlayerColor.RED if color == PlayerColor.BLUE else PlayerColor.BLUE)
    if (maximize==True):
        best = float('-inf')
        for child in node.children:
            child.add_children()
            child_eval = alpha_beta(child, depth-1, alpha, beta, False, PlayerColor.RED if color == PlayerColor.BLUE else PlayerColor.BLUE)
            best = max(best, child_eval)
            alpha = max(alpha, best)
            if beta<=alpha:
                break
        return best
    else:
        worst = float('inf')
        child_len = len(node.children)
        for child in node.children:
            child.add_children()
            child_eval = alpha_beta(child, depth-1, alpha, beta, True, PlayerColor.RED if color == PlayerColor.BLUE else PlayerColor.BLUE)
            worst = min(beta, child_eval)
            beta = min(beta, worst)
            if beta<=alpha:
                break
        return worst

def minimax_with_alpha_beta(node: ABNode, color:PlayerColor, depth:int):
    values = dict()
    for child in node.children:
        child.add_children()
        values.update({child.action: alpha_beta(child,depth,float('-inf'),float('inf'), False, color)})
    choices = []
    best_eval = max(values.values())
    for action in values.keys():
        if values[action] == best_eval:
            choices.append(action)
    return random.choice(choices)

def eval(board: MatrixBoard, color: PlayerColor):
    if color == PlayerColor.RED:
        return board.red_power-board.blue_power
    else:
        return board.blue_power-board.red_power