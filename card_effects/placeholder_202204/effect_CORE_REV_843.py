"""Effect for Sinfueled Golem (CORE_REV_843).

Card Text: <b>Infuse (3):</b> Gain stats equal to the Attack of the minions that <b>Infused</b> this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass