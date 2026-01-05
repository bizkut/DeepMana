"""Effect for Unpowered Mauler (BOT_098).

Card Text: Can only attack if you cast a spell this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass