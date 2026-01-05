"""Effect for Vanish (NEW1_004).

Card Text: Return all minions to their owner's hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass