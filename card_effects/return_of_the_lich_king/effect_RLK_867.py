"""Effect for Vrykul Necrolyte (RLK_867).

Card Text: [x]<b>Battlecry:</b> Give a friendly
minion "<b>Deathrattle:</b>
 Summon a 2/2 Zombie
with <b>Rush</b>."
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_867t")


def deathrattle(game, source):
    pass