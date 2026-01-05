"""Effect for Piloted Shredder (GVG_096).

Card Text: <b>Deathrattle:</b> Summon a random 2-Cost minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GVG_096t")