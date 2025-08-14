# Exercise 18-1: This exercise just wants you to draw a class diagram... no code solution here ;)


# Write a 'Deck' method called 'deal_hands()' that takes two parameters: the number of hands and the number of cards per
# hand. It should create the appropriate number of 'Hand' objects, deal the appropriate number of cards per hand, and
# return a list of 'Hands'.
import random


class Card:
    """Represents a standard playing card."""
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"

class Deck:
    """Represent a standard deck of playing cards."""

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))

        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    """Solution to the exercise."""
    def deal_hands(self, n_hands, n_cards_per_hand):
        # Dict for dealt hands. Each hand is assigned a key with a list of dealt cards as value.
        hands = {}

        self.shuffle()

        for i in range(n_hands):
            hands[i] = []
            for _ in range(n_cards_per_hand):
                hands[i].append(self.pop_card())

        return hands

class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=""):
        super().__init__()  # The book doesn't mention the super method, and it technically isn't needed in this case,
                            # but I always put it in by default when dealing with child classes.
        self.cards = []
        self.label = label


# Exercise 18-3: Exercise relies on code downloaded from http://thinkpython2.com/code, which isn't available at the time
# of writing this. Sorry.
