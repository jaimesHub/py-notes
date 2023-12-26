class Card:
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, value, suit) -> None:
        if value not in Card.values:
            raise ValueError(f"{value} does not exist")
        
        if suit not in Card.suits:
            raise ValueError(f"{suit} does not exit")
        
        self.value = value
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.value} of {self.suit}"