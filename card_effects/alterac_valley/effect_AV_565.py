"""Effect for Axe Berserker (AV_565).

Card Text: <b>Rush</b>. <b>Honorable Kill:</b>
Draw a weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)