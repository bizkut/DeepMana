"""Effect for Rattling Rascal (CORE_ICC_025).

Card Text: [x]<b>Battlecry:</b> Summon a
5/5 Skeleton.
<b>Deathrattle:</b> Summon one
for your opponent.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_ICC_025t")


def deathrattle(game, source):
    pass