"""Effect for Skyfin (DRG_072).

Card Text: <b>Battlecry:</b> If you're holding a Dragon, summon 2 random Murlocs.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_072t")