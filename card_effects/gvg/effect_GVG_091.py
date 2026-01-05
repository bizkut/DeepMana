"""Effect for Arcane Nullifier X-21 (GVG_091).

Card Text: <b>Taunt</b>
<b>Elusive</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass