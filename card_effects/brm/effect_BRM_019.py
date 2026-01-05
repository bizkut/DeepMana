"""Effect for Grim Patron (BRM_019).

Card Text: After this minion survives damage, summon another Grim Patron.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BRM_019t")