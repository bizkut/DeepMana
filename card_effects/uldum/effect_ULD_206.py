"""Effect for Restless Mummy (ULD_206).

Card Text: <b>Rush</b>
<b>Reborn</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass