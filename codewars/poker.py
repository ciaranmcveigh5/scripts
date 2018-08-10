# A famous casino is suddenly faced with a sharp decline of their revenues. They decide to offer Texas hold'em also
#  online. Can you help them by writing an algorithm that can rank poker hands?
#
# Task:
#
# Create a poker hand that has a method to compare itself to another poker hand:
#     compare_with(self, other_hand)
# A poker hand has a constructor that accepts a string containing 5 cards:
#     PokerHand(hand)
# The characteristics of the string of cards are:
# A space is used as card seperator
# Each card consists of two characters
# The first character is the value of the card, valid characters are:
# 2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
# The second character represents the suit, valid characters are:
# S(pades), H(earts), D(iamonds), C(lubs)
#
# The result of your poker hand compare can be one of these 3 options:
#     RESULT = ["Loss", "Tie", "Win"]
# Apply the Texas Hold'em rules for ranking the cards.
# There is no ranking for the suits.

import unittest

class PokerHand:

    validCardValues = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    validSuitValues = ["S", "H", "D", "C"]
    cardValueTranslation = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self):
            return

    def setHand(self, hand):
        self.hand = hand
        if not self.__isHandValid():
            raise ValueError


    def __isHandValid(self):
        cards = self.hand.split()
        if len(cards) != 5:
            return False
        for card in cards:
            cardValue = card[0]
            cardSuit = card[1]
            if cardValue not in self.validCardValues or cardSuit not in self.validSuitValues or cards.count(card) != 1:
                return False
        return True

    def compareWithOtherHand(self, oppentHand):
        return True

    def isHandStraight(self):
        cards = self.hand.split()
        values = []
        for card in cards:
            values.append(self.cardValueTranslation[card[0]])
        values = sorted(values)
        if values[len(values)-1] - values[0] == len(values)-1:
            return True
        else:
            return False

    def isHandFlush(self):
        cards = self.hand.split()
        suits = []
        for card in cards:
            suits.append(card[1])
        if all(suits[0] == suit for suit in suits):
            return True
        else:
            return False

    def checkIfHandHasPairs(self):
        return True



class TestCases(unittest.TestCase):

    def test_set_hand_accepts_valid_values(self):
        self.assertTrue(PokerHand.setHand("2S KH KD JD 5C"))

    def test_constructor_raises_error_for_invalid_values(self):
        # Value not in array
        with self.assertRaises(ValueError):
            PokerHand("0S KH KD JD 5C")
        # Value not in suits
        with self.assertRaises(ValueError):
            PokerHand("2F KH KD JD 5C")
        # Duplicate Card
        with self.assertRaises(ValueError):
            PokerHand("KH KH KD JD 5C")
        # More than 5 cards
        with self.assertRaises(ValueError):
            PokerHand("2S KH KD JD 5C QS")
        # Less than 5 cards
        with self.assertRaises(ValueError):
            PokerHand("2S KH KD JD")

    def test_is_flush_true(self):
        self.assertTrue(PokerHand("2H KH 3H JH 5H").isHandFlush())

    def test_is_flush_flase(self):
        self.assertFalse(PokerHand("2H KH 3S JH 5H").isHandFlush())

    def test_is_straight_true(self):
        self.assertTrue(PokerHand("2H 3H 4H 5H 6H").isHandStraight())
        self.assertTrue(PokerHand("9S TD JH QC KH").isHandStraight())

    def test_is_straight_false(self):
        self.assertFalse(PokerHand("2H 3H 7H 5H 6H").isHandStraight())

if __name__ == '__main__':
    unittest.main()