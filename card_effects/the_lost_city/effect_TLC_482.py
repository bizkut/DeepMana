"""Effect for Slagclaw (TLC_482).

Card Text: [x]<b>Battlecry:</b> Summon two
2/1 Sizzling Cinders.
<b>Kindred:</b> Trigger your Sizzling
Cinders' <b>Deathrattles.</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_482t")


def deathrattle(game, source):
    pass