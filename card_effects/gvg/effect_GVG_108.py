"""Effect for Recombobulator (GVG_108).

Card Text: <b>Battlecry:</b> Transform a friendly minion into a random minion with the same Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass