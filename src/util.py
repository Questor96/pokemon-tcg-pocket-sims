import copy
import random

def create_shuffled_deck(orig_deck: list) -> list:
    deck = copy.deepcopy(orig_deck)
    random.shuffle(deck)
    return deck