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
    action = input("[H]it or [S]tick? ").strip().upper()
    if action not in "HS" or len(action) != 1:
        print("I don't know how to do that")
        continue

    if action == 'H':
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

        while dealer.soft_value() < 17:
            card = deck.next()
            print("Dealer draws: " + str(card))
            dealer.add_card(card)

        print("Dealer holds: " + str(dealer))
        if player.soft_value() > dealer.soft_value() or dealer.bust():
            print("You win!!!")
        elif player.soft_value() == dealer.value():
            print("You draw!!")
        else:
            print("You lose :(")
        break
