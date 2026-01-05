"""Effect for Lady Darkvein (CORE_REV_373).

Card Text: [x]<b>Battlecry:</b> Summon two
2/1 Shades. Each gains
a <b>Deathrattle</b> to cast your 
last Shadow spell.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_373t")


def deathrattle(game, source):
    pass