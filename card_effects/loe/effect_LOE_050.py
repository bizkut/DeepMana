"""Effect for Mounted Raptor (LOE_050).

Card Text: <b>Deathrattle:</b> Summon a random 1-Cost minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOE_050t")