from enum import Enum

class Suit(Enum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3

class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 5
    FIVE = 7
    SIX = 11
    SEVEN = 13
    EIGHT = 17
    NINE = 19
    TEN = 23
    JACK = 29
    QUEEN = 31
    KING = 37
    ACE = 41


class card:
    def __init__(self,suit: Suit,rank: Rank):
        self.suit = suit
        self.rank = rank