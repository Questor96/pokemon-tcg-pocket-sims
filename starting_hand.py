from src.game_rules import (
    starting_hand_basic_first,
    starting_hand_basic_last,
    starting_hand_basic_random,
    TARGET_BASIC,
    BASIC_CARDS,
    OTHER_CARD
)
from src.util import create_shuffled_deck

"""
Comparison of the number of basics in starting hand,
  based on the different algorithmic ways to draw a starting hand
  1) Guarantee a basic, then draw 3 cards
  2) Draw 3 cards, then draw a basic if no basics drawn yet
  3) Draw 4 cards, then mulligan if no basics drawn
"""

def trial_num_basics_first(orig_deck):
    deck = create_shuffled_deck(orig_deck)
    hand = []
    starting_hand_basic_first(deck, hand)
    return len([card for card in hand if card in BASIC_CARDS])

def trial_num_basics_last(orig_deck):
    deck = create_shuffled_deck(orig_deck)
    hand = []
    starting_hand_basic_last(deck, hand)
    return len([card for card in hand if card in BASIC_CARDS])

def trial_num_basics_random(orig_deck):
    deck = create_shuffled_deck(orig_deck)
    hand = []
    starting_hand_basic_random(deck, hand)
    return len([card for card in hand if card in BASIC_CARDS])

def starting_hand_odds():
    basics = 7
    other_cards = 20 - basics
    print(f"{basics=}")
    print(f"{other_cards=}")

    deck = [TARGET_BASIC] * basics
    deck += [OTHER_CARD] * other_cards

    repetition = 10000000
    print(f"{repetition=}")

    sum = 0
    for _ in range(repetition):
        sum += trial_num_basics_first(deck)
    print("Basic check as first card: ", sum/repetition)

    sum = 0
    for _ in range(repetition):
        sum += trial_num_basics_last(deck)
    print("Basic check on last card: ", sum/repetition)

    sum = 0
    for _ in range(repetition):
        sum += trial_num_basics_random(deck)
    print("Mulligan until basic: ", sum/repetition)


if __name__ == '__main__':
    starting_hand_odds()