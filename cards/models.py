from django.db import models


# Create your models here.

class Card(models.Model):
    SUITS = ["clubs", "diamonds", "hearts", "spades"]
    RANKS = ["ace", "2", "3", "4", "5", "6",
             "7", "8", "9", "10", "jack", "queen", "king"]
    SHORT_RANKS = ["A", "2", "3", "4", "5", "6",
             "7", "8", "9", "T", "J", "Q", "K"]
    VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # there are 52 cards with ids from 0 to 51

    def suit(self):
        return (self.id - 1) // 13  # the suits are [0..12] = clubs, [13..25] = diamonds etc

    def rank(self):
        return (self.id - 1) % 13  # the ranks are 0, 13, 26, 39 are the aces, 1, 14, 27,40 are the 2s, etc

    def __str__(self):
        return self.SUITS[int(self.suit())].upper()[0] + self.SHORT_RANKS[int(self.rank())]

    def value(self):
        return self.VALUES[self.rank()]

    def img_url(self):
        return self.RANKS[int(self.rank())] + "_of_" + self.SUITS[int(self.suit())] + ".png"


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        v = 0
        for card in self.cards:
            v += card.value()
        return v

    def __str__(self):
        output = ""
        for card in self.cards:
            output = output + str(card)
        return output

class Deck:
    # initialize with array of 52 cards shuffled

    # next pops of the first element and shunts up the rest

    def __init__(self):
        self.cards = Card.objects.all().shuffle()