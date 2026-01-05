"""Effect for Incanter's Flow (BT_002).

Card Text: Reduce the Cost of spells in your deck by (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass