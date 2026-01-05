"""Effect for Dreadsoul Corrupter (EDR_841).

Card Text: [x]<b>Battlecry and Deathrattle:</b>
Summon a random
<b>Dormant</b> Dreadseed.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_841t")


def deathrattle(game, source):
    pass