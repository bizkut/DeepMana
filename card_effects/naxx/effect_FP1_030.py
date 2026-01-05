"""Effect for Loatheb (FP1_030).

Card Text: <b>Battlecry:</b> Enemy spells cost (5) more next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass