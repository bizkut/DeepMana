"""Effect for Wobbling Runts (LOE_089).

Card Text: <b>Deathrattle:</b> Summon three 2/2 Runts.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOE_089t")