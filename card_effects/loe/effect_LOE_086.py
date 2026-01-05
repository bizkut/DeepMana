"""Effect for Summoning Stone (LOE_086).

Card Text: Whenever you cast a spell, summon a random minion of the same Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOE_086t")