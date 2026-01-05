"""Effect for Imprisoned Scrap Imp (BT_305).

Card Text: <b>Dormant</b> for 2 turns.
When this awakens,
give all minions in your hand +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2