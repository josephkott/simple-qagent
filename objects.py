#!/usr/local/bin/python3
import sys
import colorama


class GameObject:
    def __init__(self, populated=False):
        self.background = colorama.Back.CYAN
        self.populated = populated

    def populate(self):
        self.populated = True

    def depopulate(self):
        self.populated = False

    def is_populated(self):
        return self.populated
    
    def show(self, symbol):
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
        agent.rest = min(agent.rest + 5, 20)


class Factory(GameObject): 
    def show(self):
        super(Factory, self).show('C')
    
    def affect(self, agent):
        agent.food -= 2
        agent.rest -= 2
        agent.creds = min(agent.creds + 1, 20)


class Shop(GameObject):
    def show(self):
        super(Shop, self).show('F')
    
    def affect(self, agent):
        agent.rest -= 1
        if agent.creds > 0:
            agent.food = min(agent.food + 5, 20)
            agent.creds -= 1
        else:
            agent.food -= 1
