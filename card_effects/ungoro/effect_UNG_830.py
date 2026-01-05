"""Effect for Cruel Dinomancer (UNG_830).

Card Text: [x]<b>Deathrattle:</b> Summon a
random minion you
discarded this game.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "UNG_830t")