"""Effect for Rodent Nest (SW_455).

Card Text: <b>Deathrattle:</b> Summon five 1/1 Rats.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_455t")