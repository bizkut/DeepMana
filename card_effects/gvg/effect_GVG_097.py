"""Effect for Lil' Exorcist (GVG_097).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Gain +1/+1 for each enemy <b>Deathrattle</b> minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1


def deathrattle(game, source):
    pass