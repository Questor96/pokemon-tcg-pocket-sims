from src.game_rules import (
    can_professors_research,
    professors_research,
    can_pokeball,
    pokeball,
    TARGET_BASIC,
    OTHER_BASIC,
    POKEBALL,
    PROFESSORS_RESEARCH,
    OTHER_CARD,
)
from src.util import create_shuffled_deck

"""
Comparison of the odds to get a specific "target basic",
  based on the order of playing Professors Research and Pokeball
  given they both are in your hand
  1) Professor's Research, then Pokeball
  2) Pokeball, then Professor's Research
"""


def trial_research_first(orig_deck: list):
    deck = create_shuffled_deck(orig_deck)
    hand = [PROFESSORS_RESEARCH, POKEBALL]
    # draw 2, then pokeball
    professors_research(deck, hand)
    pokeball(deck, hand)
    if can_pokeball(hand):
        pokeball(deck, hand)
    return 1 if TARGET_BASIC in hand else 0

def trial_pokeball_first(orig_deck: list):
    deck = create_shuffled_deck(orig_deck)
    hand = [PROFESSORS_RESEARCH, POKEBALL]
    # pokeball, then draw 2
    pokeball(deck, hand)
    professors_research(deck, hand)
    if can_pokeball(hand):
        pokeball(deck, hand)
    return 1 if TARGET_BASIC in hand else 0

def pokeball_vs_research():
    total_cards = 12
    target_basics = 2
    other_basics = 3
    pokeball = 0
    other_cards = total_cards - target_basics - other_basics - pokeball
    print(f"{target_basics=}")
    print(f"{other_basics=}")
    print(f"{pokeball=}")
    print(f"{other_cards=}")

    deck = [TARGET_BASIC] * target_basics
    deck += [OTHER_BASIC] * other_basics
    deck += [POKEBALL] * pokeball
    deck += [OTHER_CARD] * other_cards

    repetition = 10000000
    print(f"{repetition=}")

    sum = 0
    for _ in range(repetition):
        sum += trial_research_first(deck)
    print("Research, then Pokeball: ", sum/repetition)

    sum = 0
    for _ in range(repetition):
        sum += trial_pokeball_first(deck)
    print("Pokeball, then Research: ", sum/repetition)


if __name__ == '__main__':
    pokeball_vs_research()