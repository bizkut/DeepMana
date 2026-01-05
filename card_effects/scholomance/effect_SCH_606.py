"""Effect for Partner Assignment (SCH_606).

Card Text: Add a random 2-Cost and 3-Cost Beast to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass