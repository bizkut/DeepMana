"""Effect for Bolvar Fordragon (GVG_063).

Card Text: Whenever a friendly minion dies while this is in your hand, gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1