"""Effect for Imprisoned Gan'arg (BT_121).

Card Text: <b>Dormant</b> for 2 turns.
When this awakens,
equip a 3/2 Axe.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass