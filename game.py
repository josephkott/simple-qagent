#!/usr/local/bin/python3
from numpy.random import randint

from objects import Home, Street, Factory, Shop
from agent import Agent

class Game:
    def __init__(self):
        self.desk_width = 3
        self.desk_height = 3
        self.desk = [
            [Home(),   Street(), Factory()],
            [Street(), Street(), Street() ],
            [Street(), Street(), Shop()   ],
        ]
        self.state_size = self.desk_height * self.desk_width * 21 * 21 * 21

    def create_agent(self):
        self.turns = 0
        self.agent = Agent(food=10, rest=10, creds=10)
        i, j = randint(self.desk_height), randint(self.desk_width)
        self.agent.set_position(i, j)
        self.desk[i][j].populate()

    def encode(self):
        """
        Encode each game state to a unique number. This numbers are used in Q - table (as row indices).
        """
        i, j = self.agent.get_position()
        code = self.agent.food
        code *= 21
        code += self.agent.rest
        code *= 21
        code += self.agent.creds
        code *= self.desk_width
        code += j
        code *= self.desk_height
        code += i
        return code
    
    def decode(self, code):
        """
        Decode game state from a number.
        """
        out = []
        out.append(code % self.desk_height)
        code = code // self.desk_height
        out.append(code % self.desk_width)
        code = code // self.desk_width
        out.append(code % 21)
        code = code // 21
        out.append(code % 21)
        code = code // 21
        out.append(code)
        return list(out)

    def show(self):
        for row in self.desk:
            for game_object in row:
                game_object.show()
            print('')
        
        print('F: %i R: %i $: %i TURN: %i' % (self.agent.food, self.agent.rest, self.agent.creds, self.turns))

    def is_over(self):
        return self.agent.is_dead()
    
    def is_action_valid(self, action):
        i, j = self.agent.get_position()
        return (0 <= i + action.di < self.desk_height) and (0 <= j + action.dj < self.desk_width)

    def act(self, action):
        self.turns += 1
        confidence = self.agent.get_confidence()

        i, j = self.agent.get_position()
        if self.is_action_valid(action):
            self.desk[i][j].depopulate()
            self.desk[i + action.di][j + action.dj].populate()   
            i, j = self.agent.act(action)

        self.desk[i][j].affect(self.agent)
        if self.agent.is_dead():
            self.desk[i][j].depopulate()
            return -10
        else:
            confidence_next = self.agent.get_confidence()
            return confidence_next - confidence