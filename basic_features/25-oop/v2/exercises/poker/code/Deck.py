import itertools
import random
from Card import Card

class Deck:
    def __init__(self) -> None:
        "Each instance of Deck should have a cards attribute with all 52 possible instances of Card."
        self.cards = list(itertools.product(Card.values, Card.suits))

    def count(self):
        "returns a count of how many cards remain in the deck."
        return len(self.cards)
    
    def __repr__(self) -> str:
        """return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)"""
        return f"Deck of {self.count()} cards"
    
    def _deal(self, number):
        """accepts a number and removes at most that many cards from the end of the deck
        If there are no cards left, this method should raise a ValueError with the message 
        "All cards have been dealt".
        """
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        
        if self.count() - number < 0:
            raise ValueError("No enough card to deal")
        
        # dealed_cards = self.cards[:number]
        self.cards = self.cards[number:]
        # return dealed_cards

        if number == 1:
            return Card(self.cards[0][0], self.cards[0][1])
        else:
            return [Card(self.cards[card_idx][0], self.cards[card_idx][1]) for card_idx in range(number)]
    
    def shuffle(self):
        """shuffle a full deck of cards. 
        If there are cards missing from the deck, 
        this method should raise a ValueError with the message "Only full decks can be shuffled".
        return the shuffled deck
        """
        total_cards = 52
        if self.count() < total_cards:
            raise ValueError("Only full decks can be shuffled")
        
        return random.shuffle(self.cards)
    
    def deal_card(self):
        """deal a single card from the deck and return that single card.
        """
        return self._deal(1)
    
    def deal_hand(self, number):
        """ accepts a number
        deal a list of cards from the deck and return that list of cards.
        """
        return self._deal(number)
    

        
