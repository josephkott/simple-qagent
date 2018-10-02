#!/usr/local/bin/python3
import sys
import colorama

from agent import Agent


class GameObject:
    def __init__(self, populated=False):
        self.background = colorama.Back.CYAN # a cell is highlighted when agent is there
        self.populated = populated # indicate if agent is there

    def populate(self):
        self.populated = True

    def depopulate(self):
        self.populated = False

    def is_populated(self):
        return self.populated
    
    def show(self, symbol):
        """
        Simple console visualisation with colorama.
        """
        if self.is_populated():
            sys.stdout.write(' ' + self.background + symbol + colorama.Style.RESET_ALL + ' ')
        else:
            sys.stdout.write(' ' + symbol + ' ')


class Street(GameObject): 
    def show(self):
        super(Street, self).show(' ')
    
    def affect(self, agent):
        agent.food -= 1
        agent.rest -= 1


class Home(GameObject):
    def show(self):
        super(Home, self).show('R')
    
    def affect(self, agent):
        agent.food -= 1
        agent.rest = min(agent.rest + 5, Agent.MAX_REST)


class Factory(GameObject): 
    def show(self):
        super(Factory, self).show('C')
    
    def affect(self, agent):
        agent.food -= 2
        agent.rest -= 2
        agent.creds = min(agent.creds + 1, Agent.MAX_CREDS)


class Shop(GameObject):
    def show(self):
        super(Shop, self).show('F')
    
    def affect(self, agent):
        agent.rest -= 1
        if agent.creds > 0:
            agent.food = min(agent.food + 5, Agent.MAX_REST)
            agent.creds -= 1
        else:
            agent.food -= 1
