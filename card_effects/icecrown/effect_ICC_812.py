"""Effect for Meat Wagon (ICC_812).

Card Text: [x]<b>Deathrattle:</b> Summon a
minion from your deck
with less Attack than
this minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ICC_812t")