"""Effect for Undertaker (FP1_028).

Card Text: Whenever you summon a minion with <b>Deathrattle</b>, gain +1/+1.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "FP1_028t")