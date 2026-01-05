"""Effect for Khadgar (DAL_575).

Card Text: Your cards that summon minions summon twice as many.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_575t")