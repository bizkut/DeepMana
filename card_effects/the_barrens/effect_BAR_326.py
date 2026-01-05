"""Effect for Razorfen Beastmaster (BAR_326).

Card Text: <b>Deathrattle:</b> Summon a <b>Deathrattle</b> minion that costs (4) or less from your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_326t")