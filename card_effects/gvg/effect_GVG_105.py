"""Effect for Piloted Sky Golem (GVG_105).

Card Text: <b>Deathrattle:</b> Summon a random 4-Cost minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GVG_105t")