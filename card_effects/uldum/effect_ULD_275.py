"""Effect for Bone Wraith (ULD_275).

Card Text: <b>Taunt</b>
<b>Reborn</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass