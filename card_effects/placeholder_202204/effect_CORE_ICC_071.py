"""Effect for Light's Sorrow (CORE_ICC_071).

Card Text: After a friendly minion loses <b>Divine Shield</b>, gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1