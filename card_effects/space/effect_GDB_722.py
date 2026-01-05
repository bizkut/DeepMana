"""Effect for Crimson Commander (GDB_722).

Card Text: Battlecry and Deathrattle: Give all Draenei in your hand +1/+1.
"""

def battlecry(game, source, target):
    player = source.controller
    
    # Give all Draenei in hand +1/+1
    for card in player.hand:
        if hasattr(card, 'data') and 'DRAENEI' in str(getattr(card.data, 'race', '')):
            card._attack += 1
            card._health += 1
            card._max_health += 1


def deathrattle(game, source):
    player = source.controller
    
    # Give all Draenei in hand +1/+1
    for card in player.hand:
        if hasattr(card, 'data') and 'DRAENEI' in str(getattr(card.data, 'race', '')):
            card._attack += 1
            card._health += 1
            card._max_health += 1