"""Effect for Master of Ceremonies (AT_117).

Card Text: <b>Battlecry:</b> If you have a minion with <b>Spell Damage</b>, gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2