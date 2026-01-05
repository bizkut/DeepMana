"""Effect for Silent Knight (AT_095).

Card Text: <b>Stealth</b>
<b>Divine Shield</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass