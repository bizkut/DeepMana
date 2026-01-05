"""Effect for Al'ar (BT_735).

Card Text: <b>Deathrattle</b>: Summon a
 0/3 Ashes of Al'ar that resurrects this minion on your next turn.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_735t")