"""Effect for Auspicious Spirits (DMF_186).

Card Text: Summon a random
4-Cost minion.
<b>Corrupt:</b> Summon a
7-Cost minion instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_186t")