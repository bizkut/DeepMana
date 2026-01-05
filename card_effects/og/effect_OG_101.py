"""Effect for Forbidden Shaping (OG_101).

Card Text: Spend all your Mana. Summon a random minion that costs that much.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "OG_101t")