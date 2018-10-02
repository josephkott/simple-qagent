#!/usr/local/bin/python3
from math import log10

class Agent:
    """
    This class represents a game agent. It has 3 resources: food, rest, and credits. Agent acts in the world trying to
    stay alive as long as possible.
    """
    MAX_FOOD = 20
    MAX_REST = 20
    MAX_CREDS = 20

    def __init__(self, food, rest, creds):
        self.food = food
        self.rest = rest
        self.creds = creds
    
    def set_position(self, i, j):
        self.i = i
        self.j = j
    
    def get_position(self):
        return self.i, self.j

    def act(self, action):
        """
        In a scope of this simple task I consider only movement actions.
        """
        self.i += action.di
        self.j += action.dj
        return self.i, self.j
    
    def is_dead(self):
        """
        If food or rest is over, agent died. 
        """
        return self.food <= 0 or self.rest <= 0
    
    def get_confidence(self):
        """
        In order to use Q - learning technic we need to distribute some reward. For this purpose I introduce so called
        confidence >= 0. After every turn agent compute delta confidence and it becames his reward at this turn.
        """
        return log10((1 + self.food) * (1 + self.rest))
