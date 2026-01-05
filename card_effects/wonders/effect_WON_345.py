"""Effect for Valstann Staghelm (WON_345).

Card Text: [x]<b>Deathrattle:</b> Summon
a <b>Taunt</b> minion from
your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_345t")