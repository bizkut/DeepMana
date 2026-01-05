"""Effect for Jewel of N'Zoth (DMF_084).

Card Text: Summon three friendly <b>Deathrattle</b> minions that died this game.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_084t")