"""Implementation game"""
############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Requirement
## https://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
BLACK_JACK_SCORE = 21
ACE = 11


def playing_black_jack():
    """playing_black_jack _summary_
    Implementing game
    """

    print(art.logo)

    computer = [random.choice(cards), random.choice(cards)]
    user = [random.choice(cards), random.choice(cards)]

    comp_score = sum(computer)
    user_score = sum(user)

    if comp_score == BLACK_JACK_SCORE:
        print("Blackjack! You went over. You lose 😭")
        return

    if comp_score > 21:
        while ACE in computer:
            computer[computer.index(ACE)] = 1
        comp_score = sum(computer)

    if user_score == BLACK_JACK_SCORE:
        print("Blackjack! Opponent went over. You win 😁")
        return

    if user_score > 21:
        while ACE in user:
            user[user.index(ACE)] = 1
        print(user)
        user_score = sum(user)

    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computer's first card: {computer[0]}")

    while True:
        user_answer = input("Type 'y' to get another card, type 'n' to pass: ")

        if user_answer == "n":
            while comp_score < 21:
                new_card = random.choice(cards)
                computer.append(new_card)
                comp_score = sum(computer)

            print(f"Your final hand: {user}, final score: {user_score}")
            print(f"Computer's final hand: {computer}, final score: {comp_score}")

            if user_score <= 21 and comp_score > 21:
                print("Opponent went over. You win 😁")

            if user_score < comp_score and comp_score <= 21:
                print("You went over. You lose 😭")

            if user_score > comp_score and user_score <= 21:
                print("Opponent went over. You win 😁")

            if user == comp_score:
                print("Draw")
            break
        else:
            new_user_card = random.choice(cards)
            user.append(new_user_card)
            user_score = sum(user)

            new_comp_card = random.choice(cards)
            computer.append(new_comp_card)
            comp_score = sum(computer)

            print(f"Your cards: {user}, current score: {user_score}")
            print(f"Computer's first card: {computer[0]}")

            if user_score > 21:
                print(f"Your final hand: {user}, final score: {user_score}")
                print(f"Computer's final hand: {computer}, final score: {comp_score}")

                print("You went over. You lose 😭")

                break


if __name__ == "__main__":
    while True:
        answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        if answer == "n":
            print("Bye!")
            break

        playing_black_jack()
