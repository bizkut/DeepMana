"""Effect for Stormwind Avenger (ONY_020).

Card Text: After you cast a spell on this minion, it gains +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2