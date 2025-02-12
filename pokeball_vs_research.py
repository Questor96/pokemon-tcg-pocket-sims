from src.game_rules import (
    professors_research,
    pokeball,
    TARGET_BASIC,
    OTHER_BASIC,
    OTHER_CARD,
)
from src.util import create_shuffled_deck


def pokeball_vs_research():
    # trials
    def trial_research_first(orig_deck: list):
        deck = create_shuffled_deck(orig_deck)
        hand = []
        # draw 2, then pokeball
        professors_research(deck, hand)
        pokeball(deck, hand)
        return 1 if TARGET_BASIC in hand else 0

    def trial_pokeball_first(orig_deck: list):
        deck = create_shuffled_deck(orig_deck)
        hand = []
        # pokeball, then draw 2
        pokeball(deck, hand)
        professors_research(deck, hand)
        return 1 if TARGET_BASIC in hand else 0
    
    # 2 target basics, 2 other basics, 8 others
    target_basics = 1
    other_basics = 6
    other_cards = 4
    print(f"{target_basics=}")
    print(f"{other_basics=}")
    print(f"{other_cards=}")

    deck = [TARGET_BASIC] * target_basics
    deck += [OTHER_BASIC] * other_basics 
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