"""Effect for Drakefire Amulet (ONY_029).

Card Text: <b>Tradeable</b>
<b>Discover</b> 2 Dragons. Summon them.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ONY_029t")