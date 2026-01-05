"""Effect for Dinomancy (UNG_917).

Card Text: Replace your Hero Power with 'Give a Beast +3/+3.'
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3