"""Effect for Giant Anaconda (UNG_086).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Summon
a minion from your hand with 5 or more Attack.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "UNG_086t")