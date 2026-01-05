"""Effect for Silverware Golem (WON_098).

Card Text: If you discard this minion, summon it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_098t")