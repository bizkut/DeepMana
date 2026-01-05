"""Effect for Devoted Maniac (DRG_050).

Card Text: <b>Rush</b>
<b>Battlecry:</b> <b>Invoke</b> Galakrond.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass