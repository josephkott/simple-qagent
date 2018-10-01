#!/usr/local/bin/python3
# In this file possible actions are represented. There only 5 movement actions in the game.

class Action:
    pass


class Stay(Action):
    di = 0
    dj = 0


class MoveUp(Action):
    di = -1
    dj = 0


class MoveDown(Action):
    di = +1
    dj = 0


class MoveLeft(Action):
    di = 0
    dj = -1


class MoveRight(Action):
    di = 0
    dj = +1


POSSIBLE_ACTIONS = [Stay, MoveUp, MoveDown, MoveLeft, MoveRight]

#  This indices are used in Q - table (as column indices).
ACTION_TO_INDEX = {action: index for index, action in enumerate(POSSIBLE_ACTIONS)}
