"""Effect for Fel Summoner (BT_509).

Card Text: <b>Deathrattle:</b> Summon a random Demon from your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_509t")