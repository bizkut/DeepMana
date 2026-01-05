"""Effect for Temple Berserker (ULD_185).

Card Text: <b>Reborn</b>
Has +2 Attack while damaged.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2