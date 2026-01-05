"""Effect for High Cultist Herenn (TLC_810).

Card Text: [x]<b>Battlecry:</b> Summon two
<b>Deathrattle</b> minions from
your deck. They fight!
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_810t")


def deathrattle(game, source):
    pass