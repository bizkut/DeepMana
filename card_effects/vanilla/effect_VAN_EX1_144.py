"""Effect for Shadowstep (VAN_EX1_144).

Card Text: Return a friendly minion to your hand. It costs (2) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass