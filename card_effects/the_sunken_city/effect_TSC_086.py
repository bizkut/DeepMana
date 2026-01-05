"""Effect for Swordfish (TSC_086).

Card Text: <b>Battlecry:</b> <b>Dredge</b>.
If it's a Pirate, give this weapon and the Pirate +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2