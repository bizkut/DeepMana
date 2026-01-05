"""Effect for Amorphous Slime (RLK_540).

Card Text: <b>Battlecry:</b> Discard a
random Undead.
<b>Deathrattle:</b> Summon a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_540t")


def deathrattle(game, source):
    pass