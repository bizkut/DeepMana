"""Effect for Conjurer's Calling (DAL_177).

Card Text: <b>Twinspell</b>
Destroy a minion. Summon 2 minions of the same Cost to replace it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_177t")