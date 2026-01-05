"""Effect for Dragonkin Sorcerer (BRM_020).

Card Text: Whenever <b>you</b> target this minion with a spell, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1