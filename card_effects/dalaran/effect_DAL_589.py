"""Effect for Hunting Party (DAL_589).

Card Text: Copy all Beasts in your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass