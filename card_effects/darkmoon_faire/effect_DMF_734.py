"""Effect for Greybough (DMF_734).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Give a random
friendly minion "<b>Deathrattle:</b>
Summon Greybough."
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_734t")