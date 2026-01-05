"""Effect for Temporal Traveler (TIME_434).

Card Text: [x]<b>Deathrattle:</b> Summon a
4/1 Shadow that attacks a
random enemy minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_434t")