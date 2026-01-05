"""Effect for Guff Runetotem (BAR_720).

Card Text: After you cast a Nature spell, give another friendly minion +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2