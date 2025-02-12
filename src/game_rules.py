import random

# constants
TARGET_BASIC = 'target_basic'
OTHER_BASIC = 'other_basic'
BASIC_CARDS = [TARGET_BASIC, OTHER_BASIC]
TARGET_STAGE1 = 'target_stage1'
OTHER_STAGE1 = 'other_stage1'
STAGE1_CARDS = [TARGET_STAGE1, OTHER_STAGE1]
TARGET_STAGE2 = 'target_stage2'
OTHER_STAGE2 = 'other_stage2'
STAGE2_CARDS = [TARGET_STAGE2, OTHER_STAGE2]
POKEMON_CARDS = [
    TARGET_BASIC,
    TARGET_STAGE1,
    TARGET_STAGE2,
    OTHER_BASIC,
    OTHER_STAGE1,
    OTHER_STAGE2
]
POKEBALL = 'pokeball'
POKEMON_COMMUNICATION = 'pkmn_comm'
PROFESSORS_RESEARCH = 'prof_rsch'

OTHER_CARD = 'o'

# card/game effects
"""
Basic Draw
"""
def draw(deck: list, hand: list):
    hand.append(deck.pop())

"""
Pokeball
"""
def can_pokeball(hand):
    return POKEBALL in hand

def pokeball(deck: list, hand: list):
    hand.remove(POKEBALL)
    
    # find a valid card
    pokeball_target_indexes = [
        index for index in list(range(len(deck))) 
        if deck[index] in BASIC_CARDS]
    if not pokeball_target_indexes:
        return  # no change to deck or hand
    
    pokeball_choice = random.choice(pokeball_target_indexes)
    # modify card zones
    hand.append(deck.pop(pokeball_choice))

"""
Pokemon Communication
"""
def can_pokemon_communication(hand):
    return POKEMON_COMMUNICATION in hand

def card_to_communication(hand: list) -> str | None:
    if OTHER_STAGE2 in hand:
        return OTHER_STAGE2
    if OTHER_STAGE1 in hand:
        return OTHER_STAGE1
    if OTHER_BASIC in hand:
        return OTHER_BASIC
    if hand.count(TARGET_STAGE2) > 1:
        return TARGET_STAGE2
    if hand.count(TARGET_STAGE1) > 1:
        return TARGET_STAGE1
    if hand.count(TARGET_BASIC) > 1:
        return TARGET_BASIC
    else:
        return None

def pokemon_communication(deck: list, hand: list, card: str):
    hand.remove(POKEMON_COMMUNICATION)
    
    # find a valid card
    communicator_target_indexes = [
        index for index in list(range(len(deck)))
        if deck[index] in POKEMON_CARDS
    ]
    if not communicator_target_indexes:
        return  # no change to deck or hand
    
    communicator_choice = random.choice(communicator_target_indexes)
    # modify card zones
    hand.remove(card)
    hand.append(deck.pop(communicator_choice))
    deck.append(card)
    random.shuffle(deck)

"""
Professor's Research
"""
def can_professors_research(hand):
    return PROFESSORS_RESEARCH in hand

def professors_research(deck: list, hand: list):
    hand.remove(PROFESSORS_RESEARCH)
    draw(deck, hand)
    draw(deck, hand)

"""
Draw Starting Hand
"""
def starting_hand_basic_first(deck: list, hand: list):
    pokeball(deck, hand)
    draw(deck, hand)
    draw(deck, hand)
    draw(deck, hand)

def starting_hand_basic_last(deck: list, hand: list):
    draw(deck, hand)
    draw(deck, hand)
    draw(deck, hand)
    if not any(card in BASIC_CARDS for card in hand):
        pokeball(deck, hand)
    else:
        draw(deck, hand)

def starting_hand_basic_random(deck: list, hand: list):
    draw(deck, hand)
    draw(deck, hand)
    draw(deck, hand)
    draw(deck, hand)
    if not any(card in BASIC_CARDS for card in hand):
        draw(hand, deck)
        draw(hand, deck)
        draw(hand, deck)
        draw(hand, deck)
        random.shuffle(deck)
        starting_hand_basic_random(deck, hand)
