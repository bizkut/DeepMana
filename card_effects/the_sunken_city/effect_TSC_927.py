"""Effect for Azsharan Gardens (TSC_927).

Card Text: Give all minions in your hand +1/+1. Put a 'Sunken Gardens' on the bottom of your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1