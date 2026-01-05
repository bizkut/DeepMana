"""Effect for Ancestral Guardian (ULD_207).

Card Text: <b>Lifesteal</b>
<b>Reborn</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass