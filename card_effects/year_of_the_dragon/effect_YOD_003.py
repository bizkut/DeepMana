"""Effect for Winged Guardian (YOD_003).

Card Text: <b>Taunt</b>
<b>Reborn</b>
<b>Elusive</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass