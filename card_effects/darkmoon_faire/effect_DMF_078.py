"""Effect for Strongman (DMF_078).

Card Text: <b>Taunt</b>
<b>Corrupt:</b> This costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass