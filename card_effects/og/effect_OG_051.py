"""Effect for Forbidden Ancient (OG_051).

Card Text: <b>Battlecry:</b> Spend all your Mana. Gain +1/+1 for each Mana spent.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1