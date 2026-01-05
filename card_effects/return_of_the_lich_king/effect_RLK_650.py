"""Effect for Lingering Zombie (RLK_650).

Card Text: [x]<b>Deathrattle:</b> Summon a
1/1 Disarmed Zombie with
"<b>Deathrattle:</b> Summon
a 1/1 Zombie."
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_650t")