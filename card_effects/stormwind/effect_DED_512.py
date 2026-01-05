"""Effect for Amulet of Undying (DED_512).

Card Text: [x]<b>Tradeable</b>
Resurrect 1 friendly
<b>Deathrattle</b> minion.
<i>(Upgrades when <b>Traded</b>!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass