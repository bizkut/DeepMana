"""Effect for Dreadsteed (AT_019).

Card Text: <b>Deathrattle:</b> At the end
 of the turn, summon a Dreadsteed.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AT_019t")