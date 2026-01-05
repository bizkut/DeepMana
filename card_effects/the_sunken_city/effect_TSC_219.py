"""Effect for Xhilag of the Abyss (TSC_219).

Card Text: [x]<b>Colossal +4</b>
At the start of your turn,
increase the damage of
Xhilag's Stalks by 1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4