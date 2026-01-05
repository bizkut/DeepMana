"""Effect for Rattlegore (SCH_621).

Card Text: <b>Deathrattle:</b> Resummon this with -1/-1.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_621t")