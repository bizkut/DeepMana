"""Effect for Colossus of the Moon (ULD_721).

Card Text: <b>Divine Shield</b>
<b>Reborn</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass