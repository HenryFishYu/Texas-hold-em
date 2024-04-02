from itertools import combinations

import card
import hand

look_up_table = {}
all_cards = [card.card(suit, rank) for suit in card.Suit for rank in card.Rank]

def init():
    # init for High Card
    for card_combo in combinations(all_cards, 7):
        product = 1
        for c in card_combo:
            product *= c.rank.value
        look_up_table[product] = hand.value(hand.Rank.HIGH_CARD,product)


def calc_hand_values(card_list: list[card.card]):
    if len(card_list)!=7:
        raise Exception("the number of cards should be 7")
    result = 1
    for i in card_list:
        result*=i
    return look_up_table[result]

if __name__ == "__main__":
# do something