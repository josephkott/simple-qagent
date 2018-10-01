#!/usr/local/bin/python3
from math import log2

class Agent:
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
        self.i += action.di
        self.j += action.dj
        return self.i, self.j
    
    def is_dead(self):
        return self.food <= 0 or self.rest <= 0
    
    def get_confidence(self):
        return log2((1 + 0.1 * self.food) * (1 + 0.1 * self.rest) / 2)
