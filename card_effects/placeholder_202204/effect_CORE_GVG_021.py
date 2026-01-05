"""Effect for Mal'Ganis (CORE_GVG_021).

Card Text: Your hero is <b>Immune</b>.
Your other Demons
have +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2