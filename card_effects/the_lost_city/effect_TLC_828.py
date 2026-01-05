"""Effect for Supreme Dinomancy (TLC_828).

Card Text: Give +2/+2 to all Beasts in your hand, deck, and battlefield.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2