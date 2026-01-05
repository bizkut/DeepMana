"""Effect for Whetstone Hatchet (WC_025).

Card Text: After your hero attacks, give a minion in your hand +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1