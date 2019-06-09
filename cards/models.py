from django.db import models


# Create your models here.

class Card(models.Model):
    SUITS = ["clubs", "diamonds", "hearts", "spades"]
    RANKS = ["ace", "two", "three", "four", "five", "six",
             "seven", "eight", "nine", "ten", "jack", "queen", "king"]
    VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    suit = models.IntegerField(default=1)
    rank = models.IntegerField(default=1)
    img_url = models.CharField(max_length=200)

    def __str__(self):
        return "The " + self.RANKS.ranks[self.rank] + " of " + self.SUITS[self.suit] + " has value " + str(self.value())

    def value(self):
        return Card.VALUES[self.rank]
