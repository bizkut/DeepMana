"""Effect for Vectus (SCH_162).

Card Text: [x]<b>Battlecry:</b> Summon two
1/1 Whelps. Each gains a
<b>Deathrattle</b> from your minions
that died this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_162t")


def deathrattle(game, source):
    pass