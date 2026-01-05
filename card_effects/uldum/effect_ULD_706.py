"""Effect for Blatant Decoy (ULD_706).

Card Text: [x]<b>Deathrattle:</b> Each player
summons the lowest Cost
minion from their hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_706t")