"""Effect for Murkwater Scribe (TSC_823).

Card Text: <b>Battlecry:</b> The next spell you play costs (1) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass