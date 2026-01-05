"""Effect for Coffin Crasher (GIL_805).

Card Text: <b>Deathrattle:</b> Summon a <b>Deathrattle</b> minion from your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GIL_805t")