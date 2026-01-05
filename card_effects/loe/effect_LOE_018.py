"""Effect for Tunnel Trogg (LOE_018).

Card Text: Whenever you <b>Overload</b>, gain +1 Attack per locked Mana Crystal.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1