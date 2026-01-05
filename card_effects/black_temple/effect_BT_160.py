"""Effect for Rustsworn Cultist (BT_160).

Card Text: [x]<b>Battlecry:</b> Give your
other minions "<b>Deathrattle:</b>
Summon a 1/1 Demon."
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_160t")


def deathrattle(game, source):
    pass