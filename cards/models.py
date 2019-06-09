from django.db import models


# Create your models here.

class Card(models.Model):
    SUITS = ["clubs", "diamonds", "hearts", "spades"]
    RANKS = ["ace", "2", "3", "4", "5", "6",
             "7", "8", "9", "10", "jack", "queen", "king"]
    VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # there are 52 cards with ids from 0 to 51

    def suit(self):
        return id / 13  # the suits are [0..12] = clubs, [13..25] = diamonds etc

    def rank(self):
        return id % 13  # the ranks are 0, 13, 26, 39 are the aces, 1, 14, 27,40 are the 2s, etc

    def __str__(self):
        return "The " + self.RANKS[self.rank] + " of " + self.SUITS[self.suit] + " has value " + str(self.value())

    def value(self):
        return self.VALUES[self.rank]

    def img_url(self):
        return self.RANKS[self.rank] + "_of_" + self.SUITS[self.suit] + ".png"
