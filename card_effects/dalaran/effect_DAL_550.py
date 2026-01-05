"""Effect for Underbelly Ooze (DAL_550).

Card Text: After this minion survives damage, summon a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_550t")