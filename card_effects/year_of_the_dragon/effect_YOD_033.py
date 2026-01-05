"""Effect for Boompistol Bully (YOD_033).

Card Text: <b>Battlecry:</b> Enemy <b>Battlecry</b> cards cost (5) more next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass