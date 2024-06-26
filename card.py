from enum import Enum

class Suit(Enum):
    CLUBS = 43
    DIAMONDS = 47
    HEARTS = 53
    SPADES = 59

class Rank(Enum):
    TWO = (2,2)
    THREE = (3,3)
    FOUR = (4,5)
    FIVE = (5,7)
    SIX = (6,11)
    SEVEN = (7,13)
    EIGHT = (8,17)
    NINE = (9,19)
    TEN = (10,23)
    JACK = (11,29)
    QUEEN = (12,31)
    KING = (13,37)
    ACE = (14,41)

    def __init__(self,value:int,prime_value:int):
        self._value_ = value
        self.prime_value = prime_value


class card:
    def __init__(self,suit: Suit,rank: Rank):
        self.suit = suit
        self.rank = rank
        self.prime_value = suit.value*rank.prime_value

