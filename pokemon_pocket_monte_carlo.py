import random
import copy


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
POKEMON_COMMUNICATOR = 'pkmn_comm'
PROFESSORS_RESEARCH = 'prof_rsch'

OTHER_CARD = 'o'

# card/game effects
def pokeball(deck: list, hand: list):
    # find a valid card
    pokeball_target_indexes = [
        index for index in list(range(len(deck))) 
        if deck[index] in BASIC_CARDS]
    pokeball_choice = random.choice(pokeball_target_indexes)
    # modify card zones
    hand.append(deck.pop(pokeball_choice))

def card_to_communicator(hand: list) -> str | None:
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

def communicator(deck: list, hand: list, card: str):
    # find a valid card
    communicator_target_indexes = [
        index for index in list(range(len(deck)))
        if deck[index] in POKEMON_CARDS
    ]
    communicator_choice = random.choice(communicator_target_indexes)
    
    # modify card zones
    hand.remove(card)
    hand.append(deck.pop(communicator_choice))
    deck.append(card)
    random.shuffle(deck)

def professors_research(deck: list, hand: list):
    draw(deck, hand)
    draw(deck, hand)

def draw(deck: list, hand: list):
    hand.append(deck.pop())

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


# trials
def pokeball_vs_research():
    # trials
    def trial_research_first(orig_deck: list):
        deck = copy.deepcopy(orig_deck)
        hand = []
        random.shuffle(deck)
        # draw 2, then pokeball
        professors_research(deck, hand)
        pokeball(deck, hand)
        return 1 if TARGET_BASIC in hand else 0

    def trial_pokeball_first(orig_deck: list):
        deck = copy.deepcopy(orig_deck)
        hand = []
        random.shuffle(deck)
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

def starting_hand_odds():
    def trial_num_basics_first(orig_deck):
        deck = copy.deepcopy(orig_deck)
        hand = []
        random.shuffle(deck)
        starting_hand_basic_first(deck, hand)
        return len([card for card in hand if card in BASIC_CARDS])

    def trial_num_basics_last(orig_deck):
        deck = copy.deepcopy(orig_deck)
        hand = []
        random.shuffle(deck)
        starting_hand_basic_last(deck, hand)
        return len([card for card in hand if card in BASIC_CARDS])

    def trial_num_basics_random(orig_deck):
        deck = copy.deepcopy(orig_deck)
        hand = []
        random.shuffle(deck)
        starting_hand_basic_random(deck, hand)
        return len([card for card in hand if card in BASIC_CARDS])

    
    basics = 19
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
    #pokeball_vs_research()
    starting_hand_odds()