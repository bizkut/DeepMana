"""Effect for Lance Carrier (AT_084).

Card Text: <b>Battlecry:</b> Give a friendly minion +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2