"""Effect for Inkveil Ambusher (TID_080).

Card Text: <b>Stealth</b>
Has +3 Attack and <b>Immune</b> while attacking.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3