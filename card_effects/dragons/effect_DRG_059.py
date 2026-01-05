"""Effect for Goboglide Tech (DRG_059).

Card Text: <b>Battlecry:</b> If you control a Mech, gain +1/+1 and <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1