#!/usr/local/bin/python3
import random
import numpy
import time
import os

from IPython.display import clear_output

from game import Game
from actions import POSSIBLE_ACTIONS, ACTION_TO_INDEX


class Player:
    """
    This class represents a player, his strategy of learning and playing the game.
    """
    def __init__(self):
        # Learning rate 
        self.alpha = 0.1

        # \gamma is a parameter of Q - learing algorithm
        self.gamma = 0.9

        # We use \epsilon - gready strategy of learning 
        self.epsilon = 0.1
        
        # Number of epochs (fully played games) to study an agent
        self.epochs = 50000

        # Game to play
        self.game = Game()

        # Q - actual target of learning procedure. It's initialized with zeroes. Structure of the Q - table:
        #
        #  ...    | action_0 | action_1 | ...
        # state_0 | Q(s0,a0) |  ...
        # state_1 | Q(s1,a1) |  ...
        # state_2 |  ...     |  ...
        #  ...    |  ...     |  ...
        #
        # where Q(si,ai) is an estimated future reward.
        self.q_table = numpy.zeros((self.game.state_size, len(POSSIBLE_ACTIONS)))
    
    def train(self, interactive=False):
        for _ in range(self.epochs):
            self.game.create_agent()

            while not self.game.is_over():
                if interactive:
                    os.system('clear')
                    self.game.show()
                    time.sleep(0.1)

                state = self.game.encode()
                if random.uniform(0, 1) < self.epsilon:
                    action = random.choice(POSSIBLE_ACTIONS)
                else:
                    action = POSSIBLE_ACTIONS[numpy.argmax(self.q_table[state])]

                reward = self.game.act(action)
                next_state = self.game.encode()
                
                # Q(S, a) <- (1 - \alpha) Q(S, a) + \alpha (r + \gamma \max_{a} Q(S' | a))
                self.q_table[state, ACTION_TO_INDEX[action]] = \
                    (1 - self.alpha) * self.q_table[state, ACTION_TO_INDEX[action]] + \
                    self.alpha * (reward + self.gamma * numpy.max(self.q_table[next_state]))

        print("Training finished!\n")
    
    def play(self, interactive=False):
        for _ in range(self.epochs):
            self.game.create_agent()

            action = POSSIBLE_ACTIONS[0]

            while not self.game.is_over():
                if interactive:
                    os.system('clear')
                    self.game.show()
                    time.sleep(0.1)

                state = self.game.encode()
                action = POSSIBLE_ACTIONS[numpy.argmax(self.q_table[state])]
                self.game.act(action)


# Run `python3 player.py` to learn agent and see how it plays
if __name__ == '__main__':
    player = Player()
    player.train(interactive=False)
    player.play(interactive=True)