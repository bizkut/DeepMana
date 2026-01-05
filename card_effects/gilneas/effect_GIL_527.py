"""Effect for Felsoul Inquisitor (GIL_527).

Card Text: <b>Lifesteal</b>
<b>Taunt</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass