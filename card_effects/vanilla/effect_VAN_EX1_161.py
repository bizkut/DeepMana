"""Effect for Naturalize (VAN_EX1_161).

Card Text: Destroy a minion.
Your opponent draws 2 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)