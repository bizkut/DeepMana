"""Effect for Confessor Paletress (WON_063).

Card Text: <b>Battlecry and Inspire:</b> Summon a random <b>Legendary</b> minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_063t")