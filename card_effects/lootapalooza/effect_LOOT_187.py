"""Effect for Twilight's Call (LOOT_187).

Card Text: Summon 1/1 copies of 2 friendly <b>Deathrattle</b> minions
that died this game.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_187t")