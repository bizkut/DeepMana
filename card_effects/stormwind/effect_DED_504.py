"""Effect for Wicked Shipment (DED_504).

Card Text: [x]<b>Tradeable</b>
Summon 2 1/1 Imps.
<i>(Upgrades by 2
when <b>Traded</b>!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DED_504t")