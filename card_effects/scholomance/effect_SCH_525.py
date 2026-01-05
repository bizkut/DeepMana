"""Effect for In Formation! (SCH_525).

Card Text: Add 2 random <b>Taunt</b> minions to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass