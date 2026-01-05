"""Effect for Barrens Blacksmith (BAR_073).

Card Text: <b>Frenzy:</b> Give your other minions +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2