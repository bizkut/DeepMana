"""Effect for Cowardly Grunt (SW_021).

Card Text: <b>Deathrattle:</b> Summon a minion from your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_021t")