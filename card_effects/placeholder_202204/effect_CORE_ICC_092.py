"""Effect for Acherus Veteran (CORE_ICC_092).

Card Text: <b>Battlecry:</b> Give a friendly minion +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1