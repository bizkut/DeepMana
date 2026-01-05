"""Effect for Cinderfin (TLC_225).

Card Text: <b>Deathrattle:</b> Summon a 2/1 Sizzling Cinder.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_225t")