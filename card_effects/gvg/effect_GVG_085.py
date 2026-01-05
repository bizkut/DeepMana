"""Effect for Annoy-o-Tron (GVG_085).

Card Text: <b>Taunt</b>
<b>Divine Shield</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass