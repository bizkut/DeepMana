"""Effect for Teron Gorefiend (BT_126).

Card Text: [x]<b>Battlecry:</b> Destroy all
other friendly minions.
<b>Deathrattle:</b> Resummon
them with +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_126t")


def deathrattle(game, source):
    pass