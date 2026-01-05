"""Effect for Exotic Mountseller (DAL_774).

Card Text: Whenever you cast a spell, summon a random
3-Cost Beast.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_774t")