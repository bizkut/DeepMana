"""Effect for The Forest's Aid (DAL_256).

Card Text: <b>Twinspell</b>
Summon five 2/2 Treants.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_256t")