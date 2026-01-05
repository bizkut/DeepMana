"""Effect for Deathspeaker (CORE_ICC_467).

Card Text: <b>Battlecry:</b> Give a friendly minion <b>Immune</b> this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1