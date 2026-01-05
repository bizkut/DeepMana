"""Effect for Rafaam's Scheme (DAL_007).

Card Text: Summon 1 1/1 Imp. <i>(Upgrades each turn!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_007t")