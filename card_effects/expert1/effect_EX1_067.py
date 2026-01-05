"""Effect for Argent Commander (EX1_067).

Card Text: <b>Charge</b>
<b>Divine Shield</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass