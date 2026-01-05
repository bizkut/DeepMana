"""Effect for Spiteful Smith (VAN_CS2_221).

Card Text: <b>Enrage:</b> Your weapon has +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2