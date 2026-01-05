"""Effect for Schooling (TSC_631).

Card Text: Add three 1/1 Piranha
Swarmers to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass