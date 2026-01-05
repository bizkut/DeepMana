"""Effect for Annoy-o-Module (BOT_911).

Card Text: <b>Magnetic</b>
<b>Divine Shield</b>
<b>Taunt</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass