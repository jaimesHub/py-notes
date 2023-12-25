from Deck import Deck
print("Let's start playing Poker")
my_deck = Deck()
my_deck.shuffle()
card = my_deck.deal_card()
print(card)
hand = my_deck.deal_hand(5)
print("hand: ", hand)
print("Current Deck: ", my_deck)