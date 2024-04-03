import unittest
import card
import hand
import main

class TestCalcHandValues(unittest.TestCase):
    def test_high_card(self):
        player_cards = [card.card(card.Suit.HEARTS, card.Rank.KING), card.card(card.Suit.DIAMONDS, card.Rank.SEVEN)]
        community_cards = [card.card(card.Suit.CLUBS, card.Rank.FIVE), card.card(card.Suit.SPADES, card.Rank.THREE),
                           card.card(card.Suit.HEARTS, card.Rank.TWO), card.card(card.Suit.DIAMONDS, card.Rank.NINE),
                           card.card(card.Suit.CLUBS, card.Rank.JACK)]
        result = main.calc_hand_values(player_cards + community_cards)
        self.assertEqual(result.rank, hand.Rank.HIGH_CARD)

    def test_one_pair(self):
        player_cards = [card.card(card.Suit.HEARTS, card.Rank.KING), card.card(card.Suit.DIAMONDS, card.Rank.KING)]
        community_cards = [card.card(card.Suit.CLUBS, card.Rank.FIVE), card.card(card.Suit.SPADES, card.Rank.THREE),
                           card.card(card.Suit.HEARTS, card.Rank.TWO), card.card(card.Suit.DIAMONDS, card.Rank.NINE),
                           card.card(card.Suit.CLUBS, card.Rank.JACK)]
        result = main.calc_hand_values(player_cards + community_cards)
        self.assertEqual(result.rank, hand.Rank.ONE_PAIR)

if __name__ == '__main__':
    unittest.main()