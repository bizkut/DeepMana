"""Effect for Mass Resurrection (DAL_724).

Card Text: Summon 3 friendly minions that died
this game.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_724t")