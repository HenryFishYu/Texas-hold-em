from itertools import combinations
from math import prod

import card
import hand

look_up_table = {}
all_cards = [card.card(suit, rank) for suit in card.Suit for rank in card.Rank]


def init():
    def calculate_product(cards: list[card]):
        prime_values = [card.rank.prime_value for card in cards[:5]]
        return prod(prime_values)
    def get_type():
        reversed_ranks = {}
        for k, v in ranks.items():
            arr = reversed_ranks.get(v,[])
            arr.append(k)
            reversed_ranks[v] = arr

        for k, v in ranks.items():
            ranks[k] = sorted(reversed_ranks[v], key = lambda v:v.value, reverse=True)

        if 4 in reversed_ranks:
            return hand.value(hand.Rank.FOUR_OF_A_KIND, reversed_ranks[4][0].value)

        if 3 in reversed_ranks:
            if len(reversed_ranks[3])>1:
                return hand.value(hand.Rank.FULL_HOUSE, reversed_ranks[3][0].value*100+reversed_ranks[3][1].value)
            if 2 in reversed_ranks:
                return hand.value(hand.Rank.FULL_HOUSE, reversed_ranks[3][0].value*100+reversed_ranks[2][0].value)

        flush_suit = [k for k,v in suits.items() if v>=5]
        if flush_suit:
            flush_cards = [card for card in card_combo if card.suit==flush_suit[0]]
            straight_rank_value = None
            straight_ranks = [flush_cards[i:i + 5] for i in range(len(flush_cards) - 4)]
            for straight_rank in straight_ranks:
                if straight_rank[0].rank.value - straight_rank[4].rank.value == 4:
                    straight_rank_value = straight_rank[0].rank.value
                    break
            if straight_rank_value:
                return hand.value(hand.Rank.STRAIGHT_FLUSH,straight_rank_value)
            return hand.value(hand.Rank.FLUSH,calculate_product(flush_cards[:5]))

        straight_rank_value = None
        straight_ranks = [reversed_ranks[i:i + 5] for i in range(len(reversed_ranks) - 4)]
        for straight_rank in straight_ranks:
            if straight_rank[0].value - straight_rank[4].value == 4:
                straight_rank_value = straight_rank[0].value
                break

        if straight_rank_value:
            return hand.value(hand.Rank.FLUSH, straight_rank_value)

        if (3 in reversed_ranks) & (len(reversed_ranks.get(3,[]))==1) & (2 not in reversed_ranks):
            left_ranks = [card for card in card_combo if card.rank == reversed_ranks[3][0]]
            return hand.value(hand.Rank.THREE_OF_A_KIND,reversed_ranks[3][0].value*10000+left_ranks[0].rank.value*100+left_ranks[1].rank.value)

        if len(reversed_ranks.get(2,[]))>1:
            left_ranks = [card for card in card_combo if card.rank not in (reversed_ranks[2][0],reversed_ranks[2][1])]
            return hand.value(hand.Rank.TWO_PAIRS,
                             reversed_ranks[2][0].value * 10000 + reversed_ranks[2][1].value * 100 + left_ranks[0].rank.value)

        if len(reversed_ranks.get(2,[]))==1:
            left_ranks = [card for card in card_combo if card.rank != reversed_ranks[2][0]]
            return hand.value(hand.Rank.ONE_PAIR,
                             reversed_ranks[2][0].value * 1000000 + calculate_product(left_ranks[:4]))

        return hand.value(hand.Rank.HIGH_CARD,calculate_product(card_combo[:5]))

    for card_combo in combinations(all_cards, 7):
        product = 1
        ranks = {}
        suits = {}
        card_combo = sorted(card_combo,key = lambda c:c.rank.value,reverse=True)
        for c in card_combo:
            product *= c.prime_value
            ranks[c.rank] = ranks.get(c.rank, 0) + 1
            suits[c.suit] = suits.get(c.suit, 0) + 1
        look_up_table[product] = get_type()


def calc_hand_values(card_list: list[card.card]):
    if len(look_up_table)==0:
        init()
    if len(card_list) != 7:
        raise Exception("the number of cards should be 7")
    result = 1
    for i in card_list:
        result *= i.rank.prime_value
    return look_up_table[result]


if __name__ == "__main__":
    c = card.card(card.Suit.CLUBS,card.Rank.ACE)
    print(c)
