"""Effect for Recurring Villain (DAL_749).

Card Text: <b>Deathrattle:</b> If this minion has 4 or more Attack, resummon it.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_749t")