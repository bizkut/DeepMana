"""Effect for Kaldorei Priestess (EDR_970).

Card Text: [x]<b>Battlecry:</b> Give all enemy
minions -2 Attack until
your next turn. <b>Imbue</b>
your Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2