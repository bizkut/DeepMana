"""Effect for Hammer of Twilight (OG_031).

Card Text: <b>Deathrattle:</b> Summon a 4/2 Elemental.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "OG_031t")