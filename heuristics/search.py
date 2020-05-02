""" This is the collection package of search utilities and heuristic
    functions to apply on agents that use heuristics 
    Goal: Find a space that brings the most opponent cluster"""
import utils.functionality as f
from boomers.player import ExamplePlayer as Player

class Node:
    """Each node will contains a player's state and its available moves:
        parent: its predecessor state
        children: its following steps
        actions: its available actions
        player: its representing game state
        g(x) + h(x) = cost(x)
        """
    def __init__(self, parent, action, color):

        self.player = Player(color)

        self.parent = parent
        if parent != None:
            self.player.player, self.player.opponent = f.update_move(self.parent.player, self.parent.player.color, action)
        self.children = []

        self.action_done = action
        self.actions = []
        self.g = 0
        self.h = 0
        self.cost = self.g + self.h
    
    def expand(self,action):
        """Expand a node to a valid move"""
        self.children.append(Node(self, action, self.player.color))

    def propagate_back(self):
        """Return the original node's action that resulted in this node"""
        root = self.parent
        while root.parent.parent != None:
            root = root.parent
        return root.action_done

"""Node functionality evaluation"""

def nearest_opponent(player, token):
    pass

def get_direct_cost(action):
    return 0

def get_heuristics(action):
    return 0

"""Search algorithms"""

def greedy(action_list):
    """Using the greedy algorithm, choose the best action
    from the list of available moves"""
    best_action = action_list[0]
    best_cost = 0

    for action in action_list:
        cost = get_direct_cost(action) + get_heuristics(action)
        if cost > best_cost:
            best_action = action
            best_cost = cost
    return best_action

def a_star(action_list):
    pass

