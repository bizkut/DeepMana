"""Effect for Ashtongue Slayer (BT_702).

Card Text: <b>Battlecry:</b> Give a <b><b>Stealth</b>ed</b> minion +3 Attack and <b>Immune</b> this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3