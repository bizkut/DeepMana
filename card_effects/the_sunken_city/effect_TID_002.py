"""Effect for Herald of Nature (TID_002).

Card Text: <b>Battlecry:</b> If you've cast a Nature spell while holding this, give your other minions +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1