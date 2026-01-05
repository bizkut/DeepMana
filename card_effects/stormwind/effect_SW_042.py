"""Effect for Persistent Peddler (SW_042).

Card Text: <b>Tradeable</b>
<b>Deathrattle:</b> Summon a Persistent Peddler from your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_042t")