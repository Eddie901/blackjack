from cards.models import Card, Hand, Deck

player = Hand()
dealer = Hand()
deck = Deck()

player.add_card(deck.next())
player.add_card(deck.next())
print("Your hand: " + str(player))

dealer.add_card(deck.next())
print("Dealer holds: " + str(dealer))

while True:
    action = input("[T]wist or [S]tick? ").strip().upper()
    if action not in "TS" or len(action) != 1:
        print("I don't know how to do that")
        continue

    if action == 'T':
        card = deck.next()
        player.add_card(card)
        print("You drew: " + str(card))
        print("Your hand: " + str(player))
        if player.bust():
            print("You lose :(")
            break
    elif action == 'S':
        print("You stuck on: " + str(player))
        print("Dealer holds: " + str(dealer))

        while dealer.value() < 17:
            card = deck.next()
            print("Dealer draws: " + str(card))
            dealer.add_card(card)

        print("Dealer holds: " + str(dealer))
        if player.value() > dealer.value() or dealer.bust():
            print("You win!!!")
        elif player.value() == dealer.value():
            print("You win!!!")
        else:
            print("You lose :(")
        break
