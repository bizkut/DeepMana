"""Effect for Razorboar (BAR_325).

Card Text: <b>Deathrattle:</b> Summon a <b>Deathrattle</b> minion that costs (3) or less from your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_325t")