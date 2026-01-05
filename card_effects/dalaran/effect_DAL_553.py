"""Effect for Big Bad Archmage (DAL_553).

Card Text: At the end of your turn, summon a random
6-Cost minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_553t")