"""Effect for Orion, Mansion Manager (REV_515).

Card Text: After a friendly <b>Secret</b> is revealed, cast a different Mage <b>Secret</b> and gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2