from enum import Enum

class HandRank(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

class hand_value:
    def __init__(self,hand_rank: HandRank,sub_value:int):
        self.hand_rank = hand_rank
        self.sub_value = sub_value