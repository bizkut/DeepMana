"""Effect for Cobalt Scalebane (CORE_ICC_029).

Card Text: At the end of your turn, give another random friendly minion +3 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3