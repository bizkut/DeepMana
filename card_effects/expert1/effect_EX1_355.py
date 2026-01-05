"""Effect for Blessed Champion (EX1_355).

Card Text: Double a minion's Attack.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass