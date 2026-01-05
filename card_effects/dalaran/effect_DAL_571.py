"""Effect for Mysterious Blade (DAL_571).

Card Text: <b>Battlecry:</b> If you control a
<b>Secret</b>, gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1