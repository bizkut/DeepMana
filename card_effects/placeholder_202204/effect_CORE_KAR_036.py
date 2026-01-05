"""Effect for Arcane Anomaly (CORE_KAR_036).

Card Text: After you cast a spell, give this minion +1 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)